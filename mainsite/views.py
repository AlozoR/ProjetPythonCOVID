from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse

from .models import Foyer
from .forms import SignInForm


def inscription(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            # TODO: récupérer les données sur form.cleaned_data
            return HttpResponseRedirect('mainsite:success')

    else:
        form = SignInForm
    context = {
        'form': form
    }
    return render(request, 'mainsite/sign_in.html', context)


def succes_inscription(request):
    return HttpResponse('inscription terminée')
