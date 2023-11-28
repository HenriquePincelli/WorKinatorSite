from django.urls import path

from . import views

app_name = "workinator"

urlpatterns = [
    path("login/", views.Login, name="Login"),
    path("cadastroprofissionalsaude/", views.CadastroProfissionalSaude, name="CadastroProfissionalSaude"),
    path("cadastropaciente/", views.CadastroPaciente, name="CadastroPaciente"),
    path("cadastroconsulta/", views.CadastroConsulta, name="CadastroConsulta"),
    path("atualizaprofissionalsaude/", views.AtualizaProfissionalSaude, name="AtualizaProfissionalSaude"),
    path("atualizapaciente/", views.AtualizaPaciente, name="AtualizaPaciente"),
    path("atualizaconsulta/", views.AtualizaConsulta, name="AtualizaConsulta"),
    path("atualizaconsultaobservacao/", views.AtualizaConsultaObservacao, name="AtualizaConsultaObservacao"),
    path("deleteprofissionalsaude/", views.DeleteProfissionalSaude, name="DeleteProfissionalSaude"),
    path("deletepaciente/", views.DeletePaciente, name="DeletePaciente"),
    path("deleteconsulta/", views.DeleteConsulta, name="DeleteConsulta"),
    path("getprofissionalsaude/", views.GetProfissionalSaude, name="GetProfissionalSaude"),
    path('getprofissionaissaude/', views.GetProfissionaisSaude, name="GetProfissionaisSaude"),
    path("getpaciente/", views.GetPaciente, name="GetPaciente"),
    path('getpacientes/', views.GetPacientes, name="GetPacientes"),
    path("getconsulta/", views.GetConsulta, name="GetConsulta"),
    path("getconsultaspaciente/", views.GetConsultasPaciente, name="GetConsultasPaciente"),
    path("getpacientesprofissional/", views.GetPacientesProfissional, name="GetPacientesProfissional"),
    path("getconsultasprofissional/", views.GetConsultasProfissional, name="GetConsultasProfissional"),
]