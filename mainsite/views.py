from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Foyer

class DetailView(generic.DetailView):
    model = Foyer
    template_name = 'mainsite/sign_in.html'
