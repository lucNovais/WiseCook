from django.db import models

from alimentos.models import Alimento
from usuarios.models import Usuario

class Possui(models.Model):

    idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nomealimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    datavalidade = models.DateField(null=True)
    quantidade = models.DecimalField(max_digits=7, decimal_places=3)

    class Meta:
        unique_together = (("idusuario", "nomealimento","datavalidade"),)

    