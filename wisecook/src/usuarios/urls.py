from django.urls import path
from . import views
from pages.views import homescreen

urlpatterns = [
    path('', homescreen, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profileView, name='profile'),
    path('createUser/', views.createUserView, name='createUser'),
    path('editProfile/<int:pk>', views.editProfileView, name='editProfile'),
    path('edit/<int:pk>', views.update, name='edit'),
]
