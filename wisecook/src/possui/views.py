from django.shortcuts import render, redirect
from django.contrib import messages

from django.http import HttpResponse

from .models import Possui
from .forms import PossuiForm, UserPossuiForm

from django.contrib.auth.decorators import login_required

@login_required
def deleteItem(request, pk):
    alimento = Possui.objects.get(id=pk)
    alimento.delete()
    return redirect('list')

@login_required
def insertView(request, *args, **kwargs):
    form = PossuiForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = {'idusuario': request.user.id,
                'nomealimento': form.cleaned_data['nomealimento'],
                'datavalidade': form.cleaned_data['datavalidade'],
                'quantidade': form.cleaned_data['quantidade']}
        stock = UserPossuiForm(data)
        stock.save()
        return redirect('list')
        
    context = {
        'form': form
    }

    return render(request, "insertitemScreen.html", context)