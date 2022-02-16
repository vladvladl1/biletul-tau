from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('home', views.homePage, name='home'),
   path('', views.loginPage, name='login'),
   path('logout', views.logoutUser, name="logout"),
   path('choose', views.choosePage, name="choose"),
   path('register', views.registerPage, name='register'),
   path('adauga', views.adaugaEvent, name='adauga'),
   path('cumpara', views.cumparaBilet, name='cumpara'),
]