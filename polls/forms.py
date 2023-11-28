from django import forms
from django.forms import ModelForm
from colorfield.fields import ColorField
from .models import ProfissionalSaude, Paciente, Consulta
import datetime

class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de usuário', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

#Register POST's
class CadastroProfissionalSaude(forms.Form):

    codProf = forms.CharField(label="Código Profissional", help_text="Código da sua área de atuação. Exemplo: Psicólogo(CRP), Médicos(CRM).", max_length=255, error_messages={"required": "Código Profissional é obrigatório!"}, required=True)
    NomeCompleto = forms.CharField(label="Nome Completo", max_length=255, error_messages={"required": "Nome Completo é obrigatório!"}, required=True)
    Email = forms.EmailField(help_text="Insira um email existente.", error_messages={"required": "Email é obrigatório!"}, required=True)
    Login = forms.CharField(label="Login", max_length=150, error_messages={"required": "Login é obrigatório!"}, required=True)
    Senha = forms.CharField(label="Senha", max_length=128, widget=forms.PasswordInput, error_messages={"required": "Senha é obrigatória!"}, required=True)
    ConfirmarSenha = forms.CharField(label="Confirmar Senha", max_length=128, widget=forms.PasswordInput, error_messages={"required": "Por gentileza, confirme a sua senha."}, required=True)
    EnderecoConsultorio = forms.CharField(label="Endereco do Consultório", help_text="(Opcional)", widget=forms.Textarea)
    DataNascimento = forms.DateField(label="Data de Nascimento", initial=datetime.date.today, error_messages={"required": "Data de Nascimento é obrigatória!"}, required=True)
    RgCpfCnpj = forms.CharField(label="Documento", help_text="CPF/CNPJ/RG", max_length=18, error_messages={"required": "Documento é obrigatório!"}, required=True)
    Telefone = forms.CharField(label="Telefone", max_length=20)
    opcoesAbordagem = (
        ("psicanalitica", "Psicanalítica"),
        ("comportamental", "Comportamental"),
        ("cognitiva", "Cognitiva"),
        ("humanista", "Humanista"),
        ("biologica", "Biológica"),
        ("evolucionista", "Evolucionista"),
        ("sociocultural", "Socio-cultural"),
        ("psicodinamica", "Psicodinâmica"),
        ("ecologica", "Ecológica"),
        ("experimental", "Experimental"),
        ("clinica", "Clínica"),
        ("psicossocial", "Psicossocial"),
        ("outras", "Outras"),
    )
    Abordagem = forms.MultipleChoiceField(label="Abordagem", help_text="Qual(is) o(s) tipo(s) de abordagem(ns) psicológica(s) você utilizará?", choices=opcoesAbordagem, widget=forms.CheckboxSelectMultiple, required=True)
    opcoesAtendimento = (
        ("presencial", "Presencial"),
        ("remoto", "Remoto"),
        ("hibrido", "Híbrido"),
    )
    Atendimento = forms.MultipleChoiceField(label="Atendimento", help_text="Presencial/Remoto/Híbrido", choices=opcoesAtendimento, widget=forms.CheckboxSelectMultiple, required=True)
    opcoesFaixaHorario = (
        ("madrugada", "Madrugada"),
        ("matinal", "Matinal"),
        ("vespertino", "Vespertino"),
        ("noturno", "Noturno"),
    )
    FaixaHorario = forms.MultipleChoiceField(label="Faixa(s) de Horário(s) para Atendimento", choices=opcoesFaixaHorario, widget=forms.CheckboxSelectMultiple, required=True)
class CadastroProfissionalSaudeForm(ModelForm):

    email = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de Usuário'}))
    senha = forms.CharField(max_length=1000, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}))
    confirmarSenha = forms.CharField(max_length=1000, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar Senha'}))

    class Meta:
        model = ProfissionalSaude
        fields = ["CodigoProfissional", "NomeCompleto", "RG_CPF_CNPJ", "Telefone",
                  "DataNascimento", "Abordagem", "Atendimento", "EnderecoConsultorio",
                  "FaixaHorario"]

class CadastroPaciente(forms.Form):

    IDProfissional = forms.IntegerField(required=True)
    NomeCompleto = forms.CharField(label="Nome Completo do Paciente", max_length=255, error_messages={"required": "Nome Completo do Paciente é obrigatório!"}, required=True)
    Telefone = forms.CharField(label="Telefone para Contato", max_length=20)
    DataNascimento = forms.DateField(label="Data de Nascimento", initial=datetime.date.today, required=False)
    Cidade = forms.CharField(label="Cidade", max_length=255, required=False)
    opcoesDeficiencia = (
        ("defvisual", "Deficiência Visual"),
        ("defauditiva", "Deficiência Auditiva"),
        ("defmotora", "Deficiência Motora"),
        ("defcognitiva", "Deficiência Cognitiva"),
        ("defFalaLinguagem", "Deficiência de Fala e Linguagem"),
        ("defpsicossocialmental", "Deficiência Psicossocial ou Mental"),
        ("defcronicasaude", "Deficiência Crônica de Saúde"),
        ("defsensorial", "Deficiência Sensorial"),
        ("outra", "Outra"),
    )
    Deficiencia = forms.MultipleChoiceField(label="Deficiências", choices=opcoesDeficiencia, widget=forms.CheckboxSelectMultiple, required=False)
    Remedio = forms.CharField(label="O seu Paciente faz o uso de algum remédio?", widget=forms.Textarea, required=False)
    opcoesEnfermidades = (
        ("infecciosas", "Infecciosas"),
        ("cardiovasculares", "Cardiovasculares"),
        ("respiratorias", "Respiratórias"),
        ("neurologicas", "Neurológicas"),
        ("endocrinas", "Endócrinas"),
        ("gastrointestinais", "Gastrointestinais"),
        ("renais", "Renais"),
        ("musculoesqueleticas", "Musculoesqueléticas"),
        ("psiquiatricas", "Psiquiátricas"),
        ("geneticas", "Genéticas"),
        ("outra", "Outra"),
    )
    Enfermidades = forms.MultipleChoiceField(label="Enfermidades", choices=opcoesEnfermidades, widget=forms.CheckboxSelectMultiple, required=False)
    opcoesEncaminhamento = (
        ("medico", "Médico"),
        ("escolar", "Escolar"),
        ("profsaude", "Outros Profissionais de Saúde"),
        ("empresarial", "Empresarial"),
        ("assistsocial", "Assistência Social"),
        ("profsaudemental", "Profissionais da Saúde Mental"),
        ("autoprocura", "Autoprocura"),
        ("recomendacao", "Recomendação"),
        ("nenhumaOpcao", "Nenhuma das Opções"),
    )
    Encaminhamento = forms.MultipleChoiceField(label="Encaminhamento", choices=opcoesEncaminhamento, widget=forms.CheckboxSelectMultiple, required=False)
    opcoesEstadoCivil = (
        ("solteiro", "Solteiro(a)"),
        ("casado", "Casado(a)"),
        ("divorciado", "Divorciado(a)"),
        ("viuvo", "Viúvo(a)"),
        ("separado", "Separado(a)"),
        ("uniaoestavel", "União Estável (ou Convivência Marital)"),
        ("casadoseparacao", "Casado(a) com Separação de Bens"),
        ("casadouniversal", "Casado(a) sob Regime de Comunhão Universal de Bens"),
        ("casadoparcial", "Casado(a) sob Regime de Comunhão Parcial de Bens"),
        ("casadofinal", "Casado(a) sob Regime de Participação Final nos Aquestos"),
    )
    EstadoCivil = forms.MultipleChoiceField(label="Estado Civil", choices=opcoesEstadoCivil, widget=forms.CheckboxSelectMultiple, required=False)
    Cor = ColorField()
class CadastroPacienteForm(ModelForm):
    
    class Meta:
        model = Paciente
        fields = ["NomeCompleto", "Telefone", "DataNascimento", "Cidade",
                  "Deficiencia", "Remedio", "Enfermidades", "Encaminhamento",
                  "EstadoCivil", "Cor"]

class CadastroConsulta(forms.Form):

    IDPaciente = forms.IntegerField(required=True)
    IDProfissional = forms.IntegerField(required=True)
    DataHoraConsulta = forms.DateTimeField(label="Data e Hora da Consulta", initial=datetime.date.today, error_messages={"required": "Data e Hora da Consulta é obrigatória!"}, required=True)
    opcoesAtendimento = (
        ("presencial", "Presencial"),
        ("remoto", "Remoto"),
        ("indefinido", "Indefinido"),
    )
    Atendimento = forms.MultipleChoiceField(label="Atendimento", choices=opcoesAtendimento, widget=forms.CheckboxSelectMultiple, required=True)
    Valor = forms.FloatField(label="Valor da Consulta", required=False)
    Comentarios = forms.CharField(label="Algum comentário sobre o/a Paciente/Consulta", widget=forms.Textarea, required=False)
    Cor = ColorField()
class CadastroConsultaForm(ModelForm):

    IDPaciente = forms.IntegerField()

    class Meta:
        model = Consulta
        fields = ["DataHoraConsulta", "Atendimento", "Valor", "Comentarios", "Cor"]

#Register PUT's
class AtualizaProfissionalSaude(forms.Form):

    IDProfissional = forms.CharField(label="Código Profissional", help_text="Código da sua área de atuação. Exemplo: Psicólogo(CRP), Médicos(CRM).", max_length=255, error_messages={"required": "Código Profissional é obrigatório!"}, required=True)
    NomeCompleto = forms.CharField(label="Nome Completo", max_length=255, error_messages={"required": "Nome Completo é obrigatório!"}, required=True)
    Email = forms.EmailField(help_text="Insira um email existente.", error_messages={"required": "Email é obrigatório!"}, required=True)
    EnderecoConsultorio = forms.CharField(label="Endereco do Consultório", help_text="(Opcional)", widget=forms.Textarea)
    DataNascimento = forms.DateField(label="Data de Nascimento", initial=datetime.date.today, error_messages={"required": "Data de Nascimento é obrigatória!"}, required=True)
    RgCpfCnpj = forms.CharField(label="Documento", help_text="CPF/CNPJ/RG", max_length=18, error_messages={"required": "Documento é obrigatório!"}, required=True)
    Telefone = forms.CharField(label="Telefone", max_length=20)
    opcoesAbordagem = (
        ("psicanalitica", "Psicanalítica"),
        ("comportamental", "Comportamental"),
        ("cognitiva", "Cognitiva"),
        ("humanista", "Humanista"),
        ("biologica", "Biológica"),
        ("evolucionista", "Evolucionista"),
        ("sociocultural", "Socio-cultural"),
        ("psicodinamica", "Psicodinâmica"),
        ("ecologica", "Ecológica"),
        ("experimental", "Experimental"),
        ("clinica", "Clínica"),
        ("psicossocial", "Psicossocial"),
        ("outras", "Outras"),
    )
    Abordagem = forms.MultipleChoiceField(label="Abordagem", help_text="Qual(is) o(s) tipo(s) de abordagem(ns) psicológica(s) você utilizará?", choices=opcoesAbordagem, widget=forms.CheckboxSelectMultiple, required=True)
    opcoesAtendimento = (
        ("presencial", "Presencial"),
        ("remoto", "Remoto"),
        ("hibrido", "Híbrido"),
    )
    Atendimento = forms.MultipleChoiceField(label="Atendimento", help_text="Presencial/Remoto/Híbrido", choices=opcoesAtendimento, widget=forms.CheckboxSelectMultiple, required=True)
    opcoesFaixaHorario = (
        ("madrugada", "Madrugada"),
        ("matinal", "Matinal"),
        ("vespertino", "Vespertino"),
        ("noturno", "Noturno"),
    )
    FaixaHorario = forms.MultipleChoiceField(label="Faixa(s) de Horário(s) para Atendimento", choices=opcoesFaixaHorario, widget=forms.CheckboxSelectMultiple, required=True)
class AtualizaProfissionalSaudeForm(ModelForm):

    class Meta:
        model = ProfissionalSaude
        fields = ["CodigoProfissional", "NomeCompleto", "RG_CPF_CNPJ", "Telefone",
                  "DataNascimento", "Abordagem", "Atendimento", "EnderecoConsultorio",
                  "FaixaHorario"]

class AtualizaPaciente(forms.Form):

    IDPaciente = forms.IntegerField(required=True)
    NomeCompleto = forms.CharField(label="Nome Completo do Paciente", max_length=255, error_messages={"required": "Nome Completo do Paciente é obrigatório!"}, required=True)
    Telefone = forms.CharField(label="Telefone para Contato", max_length=20)
    DataNascimento = forms.DateField(label="Data de Nascimento", initial=datetime.date.today, required=False)
    Cidade = forms.CharField(label="Cidade", max_length=255, required=False)
    opcoesDeficiencia = (
        ("defvisual", "Deficiência Visual"),
        ("defauditiva", "Deficiência Auditiva"),
        ("defmotora", "Deficiência Motora"),
        ("defcognitiva", "Deficiência Cognitiva"),
        ("defFalaLinguagem", "Deficiência de Fala e Linguagem"),
        ("defpsicossocialmental", "Deficiência Psicossocial ou Mental"),
        ("defcronicasaude", "Deficiência Crônica de Saúde"),
        ("defsensorial", "Deficiência Sensorial"),
        ("outra", "Outra"),
    )
    Deficiencia = forms.MultipleChoiceField(label="Deficiências", choices=opcoesDeficiencia, widget=forms.CheckboxSelectMultiple, required=False)
    Remedio = forms.CharField(label="O seu Paciente faz o uso de algum remédio?", widget=forms.Textarea, required=False)
    opcoesEnfermidades = (
        ("infecciosas", "Infecciosas"),
        ("cardiovasculares", "Cardiovasculares"),
        ("respiratorias", "Respiratórias"),
        ("neurologicas", "Neurológicas"),
        ("endocrinas", "Endócrinas"),
        ("gastrointestinais", "Gastrointestinais"),
        ("renais", "Renais"),
        ("musculoesqueleticas", "Musculoesqueléticas"),
        ("psiquiatricas", "Psiquiátricas"),
        ("geneticas", "Genéticas"),
        ("outra", "Outra"),
    )
    Enfermidades = forms.MultipleChoiceField(label="Enfermidades", choices=opcoesEnfermidades, widget=forms.CheckboxSelectMultiple, required=False)
    opcoesEncaminhamento = (
        ("medico", "Médico"),
        ("escolar", "Escolar"),
        ("profsaude", "Outros Profissionais de Saúde"),
        ("empresarial", "Empresarial"),
        ("assistsocial", "Assistência Social"),
        ("profsaudemental", "Profissionais da Saúde Mental"),
        ("autoprocura", "Autoprocura"),
        ("recomendacao", "Recomendação"),
        ("nenhumaOpcao", "Nenhuma das Opções"),
    )
    Encaminhamento = forms.MultipleChoiceField(label="Encaminhamento", choices=opcoesEncaminhamento, widget=forms.CheckboxSelectMultiple, required=False)
    Cor = ColorField()
class AtualizaPacienteForm(ModelForm):

    IDPaciente = forms.IntegerField()

    class Meta:
        model = Paciente
        fields = ["IDPaciente", "NomeCompleto", "Telefone", "DataNascimento",
                  "Cidade", "Deficiencia", "Remedio", "Enfermidades",
                  "Encaminhamento", "EstadoCivil", "Cor"]

class AtualizaConsulta(forms.Form):

    IDConsulta = forms.IntegerField(required=True)
    DataHoraConsulta = forms.DateTimeField(label="Data e Hora da Consulta", initial=datetime.date.today, error_messages={"required": "Data e Hora da Consulta é obrigatória!"}, required=True)
    opcoesAtendimento = (
        ("presencial", "Presencial"),
        ("remoto", "Remoto"),
        ("indefinido", "Indefinido"),
    )
    Atendimento = forms.MultipleChoiceField(label="Atendimento", choices=opcoesAtendimento, widget=forms.CheckboxSelectMultiple, required=True)
    Valor = forms.FloatField(label="Valor da Consulta", required=False)
    Comentarios = forms.CharField(label="Algum comentário sobre o/a Paciente/Consulta", widget=forms.Textarea, required=False)
    Cor = ColorField()
class AtualizaConsultaForm(ModelForm):

    IDConsulta = forms.IntegerField()

    class Meta:
        model = Consulta
        fields = ["IDConsulta", "DataHoraConsulta", "Atendimento", "Valor",
                  "Comentarios", "Cor"]

class AtualizaConsultaObservacao(forms.Form):

    IDConsulta = forms.IntegerField(required=True)
    Comentarios = forms.CharField(label="Algum comentário sobre o/a Paciente/Consulta", widget=forms.Textarea, required=False)
    Cor = ColorField()
class AtualizaConsultaObservacaoForm(ModelForm):

    IDConsulta = forms.IntegerField()

    class Meta:
        model = Consulta
        fields = ["IDConsulta", "Comentarios", "Cor"]

#Register DELETE's
class DeleteProfissionalSaude(forms.Form):

    IDProfissional = forms.IntegerField(required=True)
#class DeleteProfissionalSaudeForm(ModelForm):
#
#    IDProfissional = forms.IntegerField()
#
#    class Meta:
#        model = ProfissionalSaude
#        fields = ["IDProfissional"]

class DeletePaciente(forms.Form):

    IDPaciente = forms.IntegerField(required=True)
class DeletePacienteForm(ModelForm):

    IDPaciente = forms.IntegerField()

    class Meta:
        model = Paciente
        fields = ["IDPaciente"]

class DeleteConsulta(forms.Form):

    IDConsulta = forms.IntegerField(required=True)
class DeleteConsultaForm(ModelForm):

    IDConsulta = forms.IntegerField()

    class Meta:
        model = Consulta
        fields = ["IDConsulta"]

#Register GET's
class GetProfissionalSaude(forms.Form):

    IDProfissional = forms.IntegerField(required=True)
class GetProfissionalSaudeForm(ModelForm):

    IDProfissional = forms.IntegerField()

    class Meta:
        model = ProfissionalSaude
        fields = ["IDProfissional"]

class GetPaciente(forms.Form):

    IDPaciente = forms.IntegerField(required=True)
class GetPacienteForm(ModelForm):

    IDPaciente = forms.IntegerField()

    class Meta:
        model = Paciente
        fields = ["IDPaciente"]

class GetConsulta(forms.Form):

    IDConsulta = forms.IntegerField(required=True)
class GetConsultaForm(ModelForm):

    IDConsulta = forms.IntegerField()

    class Meta:
            model = Consulta
            fields = ["IDConsulta"]

class GetConsultasPaciente(forms.Form): #Return all "Consultas" of a "Paciente"

    IDPaciente = forms.IntegerField(required=True)
class GetConsultasPacienteForm(ModelForm): #Return all "Consultas" of a "Paciente"

    IDPaciente = forms.IntegerField()
    
    class Meta:
        model = Consulta
        fields = ["IDPaciente"]

class GetPacientesProfissional(forms.Form): #Return all "Pacientes" of a "Profissional"

    IDProfissional = forms.IntegerField(required=True)
#class GetPacientesProfissionalForm(ModelForm): #Return all "Pacientes" of a "Profissional"
#
#    IDProfissional = forms.IntegerField()
#
#    class Meta:
#        model = Paciente
#        fields = ["IDProfissional"]


class GetConsultasProfissional(forms.Form): #Return all "Consultas" of a "Paciente"

    IDProfissional = forms.IntegerField(required=True)
#class GetConsultasProfissionalForm(ModelForm): #Return all "Consultas" of a "Paciente"
#
#    IDProfissional = forms.IntegerField()
#    
#    class Meta:
#        model = Consulta
#        fields = ["IDProfissional"]