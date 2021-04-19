from django.db import models

from alimentos.models import Alimento
from usuarios.models import Usuario

class Receita(models.Model):
    nome = models.CharField(max_length=50, null=False, primary_key=True)
    modopreparo = models.TextField(max_length=1000, null=False)
    
    def __str__(self):
        return(self.nome)

class Utiliza(models.Model):
    nomereceita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    nomealimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=7, decimal_places=3, null=False)

    class Meta:
        unique_together = (("nomereceita", "nomealimento"),)

class Recomendada(models.Model):
    nomereceita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    correspondencia = models.DecimalField(max_digits=7, decimal_places=3, null=False)

    class Meta:
        unique_together = (("nomereceita", "idusuario"),)