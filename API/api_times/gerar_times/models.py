from django.db import models

#python manage.py makemigrations gerar_times PREPARA O MIGRATIONS
#python manage.py migrate EXECUTA O MIGRATIONS

class Aluno(models.Model):
    Nome = models.CharField(max_length=150)
    Area_de_atuacao = models.CharField(max_length=30)
    Nivel_de_senioridade = models.CharField(max_length=10)
    Linguagem_Afinidade = models.CharField(max_length=50)
    RA = models.CharField(max_length=9, unique=True)
    Periodo = models.CharField(max_length=2)
    Email = models.CharField(max_length=50)

    class Meta:
        db_table = 'Aluno'

class Professor(models.Model):
    Email = models.CharField(max_length=50, unique=True)
    Senha = models.CharField(max_length=50)
    Nome = models.CharField(max_length=150)

    class Meta:
        db_table = 'Professor'