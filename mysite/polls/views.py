from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Question,Choice
from django.template import loader

def index(request):
    q_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'q_list' : q_list,
    }
    return HttpResponse(template.render(context,request))
def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404("Question does not exist.")
    return render(request,'polls/detail.html',{'question':question})
def results(request,question_id):
    response = "You are looking at the result of the question " + str(question_id)
    return HttpResponse(response)
def vote(request,question_id):
    return HttpResponse("You are voting on question"+ str(question_id))
