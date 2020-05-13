from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login

import logging

from .models import Foyer
from django.contrib.auth.models import User
from .forms import SignInForm, LogInForm


logger = logging.getLogger(__name__)


def inscription(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            # TODO: récupérer les données sur form.cleaned_data
            username = form.cleaned_data['username']
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            mail = form.cleaned_data['mail']
            telephone = form.cleaned_data['telephone']
            adresse = form.cleaned_data['adresse']
            ville = form.cleaned_data['ville']
            mot_de_passe = form.cleaned_data['mot_de_passe']
            habitants = form.cleaned_data['habitants']
            est_une_residence = form.cleaned_data['est_une_residence']
            user = User.objects.create_user(username=username, email=mail,
                                            password=mot_de_passe)
            user.last_name = nom
            user.first_name = prenom
            temp = int(est_une_residence)
            foyer = Foyer(user=user, adresse=adresse, ville=ville,
                          est_une_residence=temp, telephone=telephone,
                          habitants=habitants)
            user.save()
            foyer.save()
            return HttpResponseRedirect(reverse('mainsite:connexion'))

    else:
        form = SignInForm

    context = {
        'form': form
    }
    return render(request, 'mainsite/sign_in.html', context)


def connexion(request):
    error = False

    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error = True

    else:
        form = LogInForm()

    context = locals()
    return render(request, 'mainsite/login.html', context)


def succes_inscription(request):
    return HttpResponse('connexion terminée')
