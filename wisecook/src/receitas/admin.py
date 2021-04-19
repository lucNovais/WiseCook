from django.contrib import admin

from .models import Receita, Utiliza, Recomendada

admin.site.register(Receita)
admin.site.register(Utiliza)
admin.site.register(Recomendada)