from django.db import models

## Classe que cria os Alunos no banco de dados
# first_name = Nome, last_name = Sobrenome
# college_enrollment = Matricula
# birth_date = Data de Nascimento

class Aluno(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    college_enrollment = models.CharField(max_length=9)
    birth_date = models.DateField()

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")