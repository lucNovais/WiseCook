from django.db import models
# from django.contrib.postgres.fields import ArrayField

class Usuario(models.Model):
    idusuario = models.IntegerField(primary_key=True, null=False)
    nome = models.CharField(max_length=50, null=False)
    restricoes = models.CharField(max_length=50, null=True) 

    def __int__(self):
        return(self.idusuario)
