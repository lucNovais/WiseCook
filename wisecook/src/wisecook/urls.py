"""wisecook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from possui.views import insertView, deleteItem
from alimentos.views import listView
from receitas.views import feedscreen, recipescreen

urlpatterns = [
    path('insert/', insertView, name='insert'),
    path('delete/<int:pk>', deleteItem, name='delete'),
    path('', include('alimentos.urls')),    
    path('feed/', feedscreen, name='feed'),
    path('recipes/<str:pk>', recipescreen),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',include('usuarios.urls')),
]

urlpatterns += staticfiles_urlpatterns()
