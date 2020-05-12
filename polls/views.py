from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "Tu regardes le résultat sac %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse(f'Le vote est présent sur la question {question_id}')
