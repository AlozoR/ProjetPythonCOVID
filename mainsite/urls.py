from django.urls import path

from . import views

app_name = 'mainsite'
urlpatterns = [
    path('signin/', views.inscription, name='inscription'),
    path('success/', views.succes_inscription, name='bravo'),
    path('login/', views.connexion, name='connexion'),
]
