from django.db import models


# python manage.py makemigrations gerar_times PREPARA O MIGRATIONS
# python manage.py migrate EXECUTA O MIGRATIONS

class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
    Email = models.CharField(max_length=50, unique=True)
    Senha = models.CharField(max_length=50)
    Nome = models.CharField(max_length=150)

    class Meta:
        db_table = 'Professor'


class Sala(models.Model):
    id = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100)
    fk_Professor_Id = models.ForeignKey(Professor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'salas'


class Times(models.Model):
    id = models.AutoField(primary_key=True)
    fk_Salas = models.ForeignKey(Sala, on_delete=models.CASCADE)

    class Meta:
        db_table = 'times'


# class Participa(models.Model):
#     fk_Salas_Id = models.ForeignKey(Sala, on_delete=models.RESTRICT)
#     fk_Aluno_Id = models.ForeignKey(Aluno, on_delete=models.SET_NULL, null=True)
#
#     class Meta:
#         db_table = 'participa'


class Contem(models.Model):
    fk_Aluno_Id = models.ForeignKey(Aluno, on_delete=models.RESTRICT)
    fk_Times_Id = models.ForeignKey(Times, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'contem'
