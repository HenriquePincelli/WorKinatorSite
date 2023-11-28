import os
from django import setup
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from datetime import datetime

# Create your models here.
class ProfissionalSaude(models.Model):
    IDProfissional = models.AutoField(primary_key=True)
    IDRamoProfissional = models.IntegerField()
    CodigoProfissional = models.CharField(max_length=255)
    NomeCompleto = models.CharField(max_length=255)
    RG_CPF_CNPJ = models.CharField(max_length=18)
    Telefone = models.CharField(max_length=20, null=True)
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    #Email = models.CharField(max_length=255)
    #Login = models.CharField(max_length=50)
    DataNascimento = models.DateTimeField()
    FotoPerfil = models.TextField(null=True)
    #Abordagem = models.CharField(AbordagemOpcoes)
    #Atendimento = models.CharField(AtendimentoOpcoes)
    #FaixaHorario = models.CharField(FaixaHorarioOpcoes)
    EnderecoConsultorio = models.TextField(null=True)
    CreatedAt = models.DateTimeField()
    UpdatedAt = models.DateTimeField()
    Active = models.BooleanField()
    opcoesAtendimento = (
        ("presencial", "Presencial"),
        ("remoto", "Remoto"),
        ("hibrido", "Híbrido"),
    )
    Atendimento = models.CharField(max_length=255, choices=opcoesAtendimento)
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
    Abordagem = models.CharField(max_length=1000, choices=opcoesAbordagem)
    opcoesFaixaHorario = (
        ("madrugada", "Madrugada"),
        ("matinal", "Matinal"),
        ("vespertino", "Vespertino"),
        ("noturno", "Noturno"),
    )
    FaixaHorario = models.CharField(max_length=255, choices=opcoesFaixaHorario)

    def __str__(self):
        return self.NomeCompleto

    #def set_password(self, Senha):
    #    self.Senha = make_password(Senha)  # Criptografar a Senha antes de salvar no banco de dados

    #@admin.display(
    #    boolean=True,
    #    ordering="CreatedAt",
    #    description="Published recently?",
    #)
    #def was_published_recently(self):
    #    now = timezone.now()
    #    return now - datetime.timedelta(days=1) <= self.CreatedAt <= now

class Paciente(models.Model):
    IDPaciente = models.AutoField(primary_key=True)
    IDProfissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE)
    NomeCompleto = models.CharField(max_length=255)
    Telefone = models.CharField(max_length=20, null=True)
    DataNascimento = models.DateTimeField(null=True)
    Cidade = models.CharField(max_length=255, null=True)
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
    Deficiencia = models.CharField(max_length=1000, choices=opcoesDeficiencia)
    Remedio = models.TextField(null=True)
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
    Enfermidades = models.CharField(max_length=1000, choices=opcoesEnfermidades)
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
    Encaminhamento = models.CharField(max_length=255, choices=opcoesEncaminhamento)
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
    EstadoCivil = models.CharField(max_length=255, choices=opcoesEstadoCivil)
    Cor = models.CharField(max_length=255, null=True)
    CreatedAt = models.DateTimeField()
    UpdatedAt = models.DateTimeField()
    Active = models.BooleanField()

class Consulta(models.Model):
    IDConsulta = models.AutoField(primary_key=True)
    IDPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    IDProfissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE)
    DataHoraConsulta = models.DateTimeField()
    opcoesAtendimento = (
        ("presencial", "Presencial"),
        ("remoto", "Remoto"),
        ("indefinido", "Indefinido"),
    )
    Atendimento = models.CharField(max_length=255, choices=opcoesAtendimento)
    Valor = models.FloatField(null=True)
    Comprovante = models.TextField(null=True)
    Comentarios = models.TextField(null=True)
    Cor = models.CharField(max_length=255, null=True)
    CreatedAt = models.DateTimeField()
    UpdatedAt = models.DateTimeField()
    Active = models.BooleanField()