from django.contrib import auth, messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse , \
                        HttpResponseBadRequest
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from.models import ProfissionalSaude, Paciente, Consulta
from .forms import CadastroProfissionalSaudeForm, CadastroPacienteForm, CadastroConsultaForm, AtualizaProfissionalSaudeForm , \
                   AtualizaPacienteForm, AtualizaConsultaForm, DeletePacienteForm, DeleteConsultaForm, \
                   GetProfissionalSaudeForm, GetPacienteForm, GetConsultaForm, GetConsultasPacienteForm, \
                   AtualizaConsultaObservacaoForm
from datetime import datetime
import pytz

saoPauloTime = pytz.timezone("America/Sao_Paulo")

# Create your views here.
def Login(request):
    if request.method == 'POST':
        login = request.POST['login']
        senha = request.POST['senha']

        if login ==" " or senha == " ":
            messages.error(request, 'Os campos login e senha não podem ficar em branco')

        if User.objects.filter(username=login).exists():
            user = auth.authenticate(request, username=login, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect("workinator:GetConsultasPaciente")
            else:
                messages.error(request, f'Cuidado, {login}!\n Parece que seu usuário ou senha está inválido,\n verifique e tente novamente.')
        else:
            messages.error(request, 'Ops!\n Parece que você ainda não está cadastrado')

    return render(request, "polls/login.html")

#Register POST's
def CadastroProfissionalSaude(request):

    if request.method == 'POST':
        form = CadastroProfissionalSaudeForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=request.POST["username"]).exists():
                msg = f'{request.POST["username"]} Login já cadastrado.'
                status = False
                return status,msg
            if request.POST["senha"] != request.POST["confirmarSenha"]:
                msg = 'As senhas devem ser as mesmas :)'
                status = False
                return status, msg

            userData = {
                "email":request.POST["email"],
                "username":request.POST["username"],
                "password":request.POST["senha"]
            }
            user = User.objects.create_user(**userData)

            profissionalSaude = ProfissionalSaude(
                User = user,
                IDRamoProfissional = 1,
                CodigoProfissional = request.POST["CodigoProfissional"],
                NomeCompleto = request.POST["NomeCompleto"],
                EnderecoConsultorio = request.POST["EnderecoConsultorio"],
                DataNascimento = request.POST["DataNascimento"],
                RG_CPF_CNPJ = request.POST["RG_CPF_CNPJ"],
                Telefone = request.POST["Telefone"],
                Abordagem = request.POST["Abordagem"],
                Atendimento = request.POST["Atendimento"],
                FaixaHorario = request.POST["FaixaHorario"],
                CreatedAt = datetime.now(saoPauloTime),
                UpdatedAt = datetime.now(saoPauloTime),
                Active = True
            )
            profissionalSaude.save()
            user.save()
            #return redirect('workinator:GetProfissionalSaude')
            #return JsonResponse({"status": True, "msg": "Registro adicionado com sucesso."})
            #return redirect("workinator:Login")
            return render(request, "polls/login.html", {"form": form})
    else:
        form = CadastroProfissionalSaudeForm()
    return render(request, "polls/cadastroprofissionalsaude.html", {"form": form})

@login_required
def CadastroPaciente(request):

    if request.method == 'POST':
        form = CadastroPacienteForm(request.POST)
        if form.is_valid():
            profissionalSaude = get_object_or_404(ProfissionalSaude, User=request.user, Active=True)
            paciente = Paciente(
                IDProfissional = profissionalSaude,
                NomeCompleto = request.POST["NomeCompleto"],
                Telefone = request.POST["Telefone"],
                DataNascimento = request.POST["DataNascimento"],
                Cidade = request.POST["Cidade"],
                Deficiencia = request.POST["Deficiencia"],
                Remedio = request.POST["Remedio"],
                Enfermidades = request.POST["Enfermidades"],
                Encaminhamento = request.POST["Encaminhamento"],
                EstadoCivil = request.POST["EstadoCivil"],
                Cor = request.POST["Cor"],
                CreatedAt = datetime.now(saoPauloTime),
                UpdatedAt = datetime.now(saoPauloTime),
                Active = True
            )
            paciente.save()
            return redirect("workinator:GetPacientesProfissional")
            #return JsonResponse({"status": True, "msg": "Paciente adicionado com sucesso."})
    else:
        form = CadastroPacienteForm()
    return render(request, "polls/cadastropaciente.html", {'form': form})

@login_required
def CadastroConsulta(request):
    form = CadastroConsultaForm()
    if request.method == "POST":
        form = CadastroConsultaForm(request.POST)
        if form.is_valid():
            profissionalSaude = get_object_or_404(ProfissionalSaude, User=request.user, Active=True)
            paciente = get_object_or_404(Paciente, IDProfissional=profissionalSaude.IDProfissional, IDPaciente=request.POST["IDPaciente"], Active=True)
            consulta = Consulta(
                IDPaciente = paciente,
                IDProfissional = profissionalSaude,
                DataHoraConsulta = request.POST["DataHoraConsulta"],
                Atendimento = request.POST["Atendimento"],
                Valor = request.POST["Valor"],
                Comentarios = request.POST["Comentarios"],
                Cor = request.POST["Cor"],
                CreatedAt = datetime.now(saoPauloTime),
                UpdatedAt = datetime.now(saoPauloTime),
                Active = True
            )
            consulta.save()
            return redirect("workinator:GetConsultasProfissional")
            #return JsonResponse({"status": True, "msg": "Consulta adicionada com sucesso."})

    return render(request, "polls/cadastroconsulta.html", {"form": form})

#Register PUT's
@login_required
def AtualizaProfissionalSaude(request):
    form = AtualizaProfissionalSaudeForm()
    if request.method == 'POST':
        form = AtualizaProfissionalSaudeForm(request.POST)
        if form.is_valid():
            profissional_saude = get_object_or_404(ProfissionalSaude, IDProfissional=request.user.id, Active=True)

            profissional_saude.CodigoProfissional = request.POST["CodigoProfissional"]
            profissional_saude.NomeCompleto = request.POST["NomeCompleto"]
            profissional_saude.EnderecoConsultorio = request.POST["EnderecoConsultorio"]
            profissional_saude.DataNascimento = request.POST["DataNascimento"]
            profissional_saude.RG_CPF_CNPJ = request.POST["RG_CPF_CNPJ"]
            profissional_saude.Telefone = request.POST["Telefone"]
            profissional_saude.Abordagem = request.POST["Abordagem"]
            profissional_saude.Atendimento = request.POST["Atendimento"]
            profissional_saude.FaixaHorario = request.POST["FaixaHorario"]
            profissional_saude.UpdatedAt = datetime.now(saoPauloTime)
            profissional_saude.save()

            return redirect("workinator:GetProfissionalSaude")
            #return JsonResponse({"status": True, "msg": "Registro atualizado com sucesso."})
        else:
            return HttpResponseBadRequest("Erro nos dados enviados.")

    return render(request, "polls/atualizaprofissionalsaude.html", {"form": form})

@login_required
def AtualizaPaciente(request):
    form = AtualizaPacienteForm()
    if request.method == 'POST':
        form = AtualizaPacienteForm(request.POST)
        if form.is_valid():
            paciente = get_object_or_404(Paciente, IDPaciente=request.POST["IDPaciente"], Active=True)

            paciente.NomeCompleto = request.POST["NomeCompleto"]
            paciente.Telefone = request.POST["Telefone"]
            paciente.DataNascimento = request.POST["DataNascimento"]
            paciente.Cidade = request.POST["Cidade"]
            paciente.Deficiencia = request.POST["Deficiencia"]
            paciente.Remedio = request.POST["Remedio"]
            paciente.Enfermidades = request.POST["Enfermidades"]
            paciente.Encaminhamento = request.POST["Encaminhamento"]
            paciente.EstadoCivil = request.POST["EstadoCivil"]
            paciente.Cor = request.POST["Cor"]
            paciente.UpdatedAt = datetime.now(saoPauloTime)
            paciente.save()

            return redirect("workinator:GetPacientesProfissional")
            #return JsonResponse({"status": True, "msg": "Registro atualizado com sucesso."})
        else:
            return HttpResponseBadRequest("Erro nos dados enviados.")

    return render(request, "polls/atualizapaciente.html", {"form": form})

@login_required
def AtualizaConsulta(request):
    form = AtualizaConsultaForm()
    if request.method == 'POST':
        form = AtualizaConsultaForm(request.POST)
        if form.is_valid():
            consulta = get_object_or_404(Consulta, IDConsulta=request.POST["IDConsulta"], Active=True)

            consulta.DataHoraConsulta = request.POST["DataHoraConsulta"]
            consulta.Atendimento = request.POST["Atendimento"]
            consulta.Valor = request.POST["Valor"]
            consulta.Comentarios = request.POST["Comentarios"]
            consulta.Cor = request.POST["Cor"]
            consulta.UpdatedAt = datetime.now(saoPauloTime)
            consulta.save()

            return redirect("workinator:GetConsultasProfissional")
            #return JsonResponse({"status": True, "msg": "Registro atualizado com sucesso."})
        else:
            return HttpResponseBadRequest("Erro nos dados enviados.")

    return render(request, "polls/atualizaconsulta.html", {"form": form})

@login_required
def AtualizaConsultaObservacao(request):
    form = AtualizaConsultaObservacaoForm()
    if request.method == 'POST':
        form = AtualizaConsultaObservacaoForm(request.POST)
        if form.is_valid():
            consulta = get_object_or_404(Consulta, IDConsulta=request.POST["IDConsulta"], Active=True)

            consulta.Comentarios = request.POST["Comentarios"]
            consulta.Cor = request.POST["Cor"]
            consulta.UpdatedAt = datetime.now(saoPauloTime)
            consulta.save()

            return redirect("workinator:GetConsultasPaciente")
            #return JsonResponse({"status": True, "msg": "Registro atualizado com sucesso."})
        else:
            return HttpResponseBadRequest("Erro nos dados enviados.")

    return render(request, "polls/atualizaconsultaobservacao.html", {"form": form})

#Register DELETE's
@login_required
def DeleteProfissionalSaude(request):
    if request.method == 'POST':
        user = get_object_or_404(User, id=request.user.id, is_active=True)
        profissionalSaude = get_object_or_404(ProfissionalSaude, User=request.user.id, Active=True)

        user.is_active = False
        profissionalSaude.Active = False
        profissionalSaude.UpdatedAt = datetime.now(saoPauloTime)
        profissionalSaude.save()
        user.save()

        return redirect("workinator:GetProfissionalSaude")
        #return JsonResponse({"status": True, "msg": "Registro deletado com sucesso."})

    return render(request, "polls/deleteprofissionalsaude.html")

@login_required
def DeletePaciente(request):
    form = DeletePacienteForm()
    if request.method == 'POST':
        form = DeletePacienteForm(request.POST)
        if form.is_valid():
            paciente = get_object_or_404(Paciente, IDPaciente=request.POST["IDPaciente"], Active=True)

            paciente.Active = False
            paciente.UpdatedAt = datetime.now(saoPauloTime)
            paciente.save()

            return redirect("workinator:GetPacientesProfissional")
            #return JsonResponse({"status": True, "msg": "Registro deletado com sucesso."})
        else:
            return HttpResponseBadRequest("Erro nos dados enviados.")

    return render(request, "polls/deletepaciente.html", {"form": form})

@login_required
def DeleteConsulta(request):
    form = DeleteConsultaForm()
    if request.method == 'POST':
        form = DeleteConsultaForm(request.POST)
        if form.is_valid():
            consulta = get_object_or_404(Consulta, IDConsulta=request.POST["IDConsulta"], Active=True)

            consulta.Active = False
            consulta.UpdatedAt = datetime.now(saoPauloTime)
            consulta.save()

            return redirect("workinator:GetConsultasProfissional")
            #return JsonResponse({"status": True, "msg": "Registro deletado com sucesso."})
        else:
            return HttpResponseBadRequest("Erro nos dados enviados.")

    return render(request, "polls/deleteconsulta.html", {"form": form})

#Register GET's
@login_required
def GetProfissionalSaude(request):
    form = GetProfissionalSaudeForm()
    if request.method == "POST":
        profissionalSaude = get_object_or_404(ProfissionalSaude, IDProfissional=request.user.id, Active=True)
        profissionalSaudeData = {
            "IDProfissional": profissionalSaude.IDProfissional,
            "CodigoProfissional": profissionalSaude.CodigoProfissional,
            "NomeCompleto": profissionalSaude.NomeCompleto,
            "EnderecoConsultorio": profissionalSaude.EnderecoConsultorio,
            "DataNascimento": profissionalSaude.DataNascimento,
            "RG_CPF_CNPJ": profissionalSaude.RG_CPF_CNPJ,
            "Telefone": profissionalSaude.Telefone,
            "Abordagem": profissionalSaude.Abordagem,
            "Atendimento": profissionalSaude.Atendimento,
            "FaixaHorario": profissionalSaude.FaixaHorario
        }

        return JsonResponse(profissionalSaudeData)

    return render(request, "polls/getprofissionalsaude.html", {"form": form})

@login_required
def GetProfissionaisSaude(request):
    profissionalSaude = ProfissionalSaude.objects.filter(Active=True)
    profissionalSaudeData = [{
        "IDProfissional": item.IDProfissional,
        "CodigoProfissional": item.CodigoProfissional,
        "NomeCompleto": item.NomeCompleto,
        "EnderecoConsultorio": item.EnderecoConsultorio,
        "DataNascimento": item.DataNascimento,
        "RG_CPF_CNPJ": item.RG_CPF_CNPJ,
        "Telefone": item.Telefone,
        "Abordagem": item.Abordagem,
        "Atendimento": item.Atendimento,
        "FaixaHorario": item.FaixaHorario
    } for item in profissionalSaude]

    return JsonResponse(profissionalSaudeData, safe=False)
    #return render(request, "polls/getprofissionaissaude.html", {'profissionais': profissionais})

@login_required
def GetPaciente(request):
    form = GetPacienteForm()
    if request.method == "POST":
        paciente = get_object_or_404(Paciente, IDPaciente=request.POST["IDPaciente"], Active=True)
        pacienteData = {
            "NomeCompleto": paciente.NomeCompleto,
            "Telefone": paciente.Telefone,
            "DataNascimento": paciente.DataNascimento,
            "Cidade": paciente.Cidade,
            "Deficiencia": paciente.Deficiencia,
            "Remedio": paciente.Remedio,
            "Enfermidades": paciente.Enfermidades,
            "Encaminhamento": paciente.Encaminhamento,
            "EstadoCivil": paciente.EstadoCivil,
            "Cor": paciente.Cor
        }

        return JsonResponse(pacienteData)

    return render(request, "polls/getpaciente.html", {"form": form})

@login_required
def GetPacientes(request):
    #pacientes = Paciente.objects.all()
    paciente = Paciente.objects.filter(Active=True)
    pacienteData = [{
            "NomeCompleto": item.NomeCompleto,
            "Telefone": item.Telefone,
            "DataNascimento": item.DataNascimento,
            "Cidade": item.Cidade,
            "Deficiencia": item.Deficiencia,
            "Remedio": item.Remedio,
            "Enfermidades": item.Enfermidades,
            "Encaminhamento": item.Encaminhamento,
            "EstadoCivil": item.EstadoCivil,
            "Cor": item.Cor
        } for item in paciente]

    return JsonResponse(pacienteData, safe=False)
    #return render(request, 'getpacientes.html', {'pacientes': pacientes})

@login_required
def GetConsulta(request):
    form = GetConsultaForm()
    if request.method == "POST":
        consulta = get_object_or_404(Consulta, IDConsulta=request.POST["IDConsulta"], Active=True)
        consultaData = {
            "DataHoraConsulta": consulta.DataHoraConsulta,
            "Atendimento": consulta.Atendimento,
            "Valor": consulta.Valor,
            "Comentarios": consulta.Comentarios,
            "Cor": consulta.Cor
        }

        return JsonResponse(consultaData)

    return render(request, "polls/getconsulta.html", {"form": form})

@login_required
def GetConsultasPaciente(request):
    form = GetConsultasPacienteForm()
    if request.method == 'POST':
        consulta = Consulta.objects.filter(IDPaciente=request.POST["IDPaciente"], Active=True)
        consultaData = [{
            "DataHoraConsulta": item.DataHoraConsulta,
            "Atendimento": item.Atendimento,
            "Valor": item.Valor,
            "Comentarios": item.Comentarios,
            "Cor": item.Cor
        } for item in consulta]

        return JsonResponse(consultaData, safe=False)

    return render(request, "polls/getconsultaspaciente.html", {"form": form})

@login_required
def GetPacientesProfissional(request):
    #form = GetPacientesProfissionalForm()
    #if request.method == 'POST':
    paciente = Paciente.objects.filter(IDProfissional=request.user.id, Active=True)
    pacienteData = [{
        "NomeCompleto": item.NomeCompleto,
        "Telefone": item.Telefone,
        "DataNascimento": item.DataNascimento,
        "Cidade": item.Cidade,
        "Deficiencia": item.Deficiencia,
        "Remedio": item.Remedio,
        "Enfermidades": item.Enfermidades,
        "Encaminhamento": item.Encaminhamento,
        "EstadoCivil": item.EstadoCivil,
        "Cor": item.Cor
    } for item in paciente]

    return JsonResponse(pacienteData, safe=False)
    #return render(request, "polls/getpacientesprofissional.html")

@login_required
def GetConsultasProfissional(request):
    consulta = Consulta.objects.filter(IDProfissional=request.user.id, Active=True)
    consultaData = [{
        "DataHoraConsulta": item.DataHoraConsulta,
        "Atendimento": item.Atendimento,
        "Valor": item.Valor,
        "Comentarios": item.Comentarios,
        "Cor": item.Cor
    } for item in consulta]

    return JsonResponse(consultaData, safe=False)
    #return render(request, "polls/getconsultasprofissional.html")
