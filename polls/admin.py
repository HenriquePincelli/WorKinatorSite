from django.contrib import admin
from .models import ProfissionalSaude, Paciente, Consulta

#POST's
class ProfissionalSaudeCadastro(admin.ModelAdmin):
#POST
    fieldsets = [
        ("Informações de Cadastro", {"fields": ["CodigoProfissional", "NomeCompleto", "DataNascimento", "RG_CPF_CNPJ"]}),
        ("Informações Profissionais", {"fields": ["Telefone", "EnderecoConsultorio", "Abordagem", "Atendimento", "FaixaHorario"]})]
#    fieldsets = [
#        ("Informações de Cadastro", {"fields": ["Email", "Login", "Senha", "ConfirmarSenha"]})
#        ]
#GET
    list_display = ["IDProfissional", "NomeCompleto", "RG_CPF_CNPJ", "CreatedAt"]
    list_filter = ["CreatedAt"]
    search_fields = ["IDProfissional", "NomeCompleto", "RG_CPF_CNPJ"]

class PacienteCadastro(admin.ModelAdmin):
#POST
    fieldsets = [
        ("Informações Sistêmicas", {"fields": ["IDProfissional", "Cor"]}),
        ("Informações do Paciente", {"fields": ["NomeCompleto", "Telefone", "DataNascimento", "Cidade",
                                                "Deficiencia", "Remedio", "Enfermidades", "Encaminhamento"]})
    ]
#GET
    list_display = ["IDPaciente", "IDProfissional", "NomeCompleto", "CreatedAt"]
    list_filter = ["CreatedAt"]
    search_fields = ["IDPaciente", "IDProfissional", "NomeCompleto"]

class ConsultaCadastro(admin.ModelAdmin):
#POST
    fieldsets = [
        ("Informações Sistêmicas", {"fields": ["IDPaciente", "IDProfissional", "Cor"]}),
        ("Informações da Consulta", {"fields": ["DataHoraConsulta", "Atendimento", "Valor", "Comentarios"]})
    ]
#GET
    list_display = ["IDProfissional", "IDPaciente", "Cor", "CreatedAt"]
    list_filter = ["CreatedAt"]
    search_fields = ["IDProfissional", "IDPaciente"]

#Login
#POST a "Profissional Saude"
#POST a "Paciente"
#POST a "Consulta"
#GET "Profissional Saude"
#GET "Paciente"
#GETALL "Paciente" by IDProfissional
class PacienteGetAll(admin.ModelAdmin):
    list_display = ["IDPaciente", "IDProfissional", "NomeCompleto", "CreatedAt"]
    list_filter = ["CreatedAt"]
    search_fields = ["IDPaciente", "IDProfissional", "NomeCompleto"]
#GET "Consulta" by IDProfissional and IDPaciente
#GETALL "Consulta" by IDProfissional
class ConsultaGetAll(admin.ModelAdmin):
    list_display = ["NomeCompleto", "DataHoraConsulta", "Atendimento"]
    list_filter = ["DataHoraConsulta"]
    search_fields = ["NomeCompleto", "DataHoraConsulta"]
#GETALL "Consulta" by IDPaciente
class ConsultaGetAll(admin.ModelAdmin):
    list_display = ["NomeCompleto", "DataHoraConsulta", "Atendimento"]
    list_filter = ["DataHoraConsulta"]
    search_fields = ["NomeCompleto", "DataHoraConsulta"]
#GETALL "Consulta" by IDConsulta
class ConsultaGetAll(admin.ModelAdmin):
    list_display = ["NomeCompleto", "DataHoraConsulta", "Atendimento"]
    list_filter = ["DataHoraConsulta"]
    search_fields = ["NomeCompleto", "DataHoraConsulta"]
#PUT "Profissional Saude"
#PUT "Paciente"
#PUT "Consulta"
class ConsultaPut(admin.ModelAdmin):
    fieldsets = [
            ("Informações Sistêmicas", {"fields": ["IDPaciente", "IDProfissional", "Cor"]}),
            ("Informações da Consulta", {"fields": ["DataHoraConsulta", "Atendimento", "Valor", "Comentarios"]})
        ]
#DELETE "Profissional Saude"
#DELETE "Paciente"
#DELETE "Consulta"

# Register your models here.
admin.site.register(ProfissionalSaude, ProfissionalSaudeCadastro)
admin.site.register(Paciente, PacienteCadastro)
admin.site.register(Consulta, ConsultaCadastro)