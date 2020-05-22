from django.urls import path

from . import views

app_name = 'mainsite'
urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('signin/', views.inscription, name='inscription'),
    path('success/', views.menu_commande, name='commande'),
    path('login/', views.connexion, name='connexion'),
    path('logout/', views.deconnexion, name='deconnexion'),
    path('commande_succes', views.succes_commande, name='bravo')
]
