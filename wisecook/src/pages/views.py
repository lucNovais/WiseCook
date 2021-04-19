from django.shortcuts import render

def homescreen(request, *args, **kwargs):
    return render(request,"homeScreen.html",{})
