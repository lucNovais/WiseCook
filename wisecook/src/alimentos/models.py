from django.db import models

class Alimento(models.Model):

    nome = models.CharField(max_length=50, null=False, primary_key=True)
    descricao = models.CharField(max_length=50, null=False)
    medida = models.CharField(max_length=50, null=False)

    def __str__(self):
        return(self.nome)
