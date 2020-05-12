from django.urls import path

from . import views

app_name = 'mainsite'
urlpatterns = [
    path('', views.SignInForm, name='inscription'),
    path('success/', views.succes_inscription, name='bravo')
]
