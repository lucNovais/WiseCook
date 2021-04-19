from django.urls import path

# from .views import index
from . import views
from pages.views import homescreen

urlpatterns = [
    path('', homescreen, name='home'),
    path('list/', views.listView, name='list'),
]