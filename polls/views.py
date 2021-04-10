from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
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
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


"""
implementación generica del método vote, se útilizo solamente para entender el http response
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
"""



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    """ As the Python comment above points out, you should always return an HttpResponseRedirect
     after successfully dealing with POST data. This tip isn’t specific to Django; 
     it’s good Web development practice in general.
    """

    """
    We are using the reverse() function in the HttpResponseRedirect constructor in this example.
     This function helps avoid having to hardcode a URL in the view function. 
     It is given the name of the view that we want to pass control to and the variable portion 
     of the URL pattern that points to that view. In this case, using the URLconf we set up in Tutorial 3,
      this reverse() call will return a string like '/polls/3/results/'
    """


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})