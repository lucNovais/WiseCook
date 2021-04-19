from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Alimento

from possui.models import Possui

from django.contrib.auth.decorators import login_required

@login_required
def listView(request, *args, **kwargs):
    possui = Possui.objects.filter(idusuario=request.user.id)
    return render(request,"itemlistScreen.html",{'possui':possui})
