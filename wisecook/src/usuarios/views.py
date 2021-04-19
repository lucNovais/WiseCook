from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Usuario
from .forms import UsuarioForm, UsuarioFormComplete

@login_required
def createUserView(request, *args, **kwargs):
    form = UsuarioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = {
            'idusuario': request.user.id,
            'nome': form.cleaned_data['nome'],
            'restricoes': form.cleaned_data['restricoes'],
        }
        stock = UsuarioFormComplete(data)
        stock.save()
        return redirect("insert")
        
    context = {
        'form': form
    }

    return render(request, "editProfileScreen.html", context)

@login_required
def editProfileView(request, pk):
    usuario = Usuario.objects.get(idusuario = pk)
    return render(request, "update.html", {'usuario':usuario})

def update(request,pk):
    usuario = Usuario.objects.get(idusuario = pk)
    usuario.nome = request.POST.get('user_name')
    usuario.restricoes = request.POST.get('user_restricoes')
    usuario.save()
    return redirect('profile')

@login_required
def profileView(request, *args, **kwargs):
    usuario = Usuario.objects.get(idusuario=request.user.id)
    return render(request, "profileScreen.html",{'usuario':usuario})

def register(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
 
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('createUser')
    else:     
        form = UserCreationForm()
    
    context = {
        'form':form
    }
    
    return render(request, 'registerScreen.html', context)