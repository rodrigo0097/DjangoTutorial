from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404
"""
##
función curda - sin template
##
def index(request):
    latest_question_list = Question.Objects.order_by('-pub_date')[:5]
    output = ', '.join(q.question_text for q in latest_question_list)
    return HttpResponse(output)
# Create your views here.
"""

"""
##
función útilizando el HttpResponse  - útiliza render para manejar la plantilla
##
def index(request):
    latest_question_list= Question.objects.order_by('-pub_date')[:5]
    template= loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
"""


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

"""
###
el método que se útiliza abajo o implementa get_object_or_404, por lo que se 
realiza un try/ except para lanzar el 404.

###
def detail2(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExists:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

"""


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)