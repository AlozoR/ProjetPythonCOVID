from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World. Index, j'adore le zboub")


def detail(request, question_id):
    return HttpResponse(f'La question du cul : {question_id}')


def results(request, question_id):
    response = "Tu regardes le résultat sac %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse(f'Le vote est présent sur la question {question_id}')
