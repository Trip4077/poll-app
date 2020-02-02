from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Question, Choice

# Get Questions
def index(req):
    question_list = Question.objects.order_by('-publish_date')[:5]

    context = { 'questions': question_list }

    return render(req, 'polls/index.html', context)

# Show specific question and choices
def detail(req, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does Not Exist")

    return render(req, 'polls/detail.html', { 'question': question })

# Display results
def results(req, question_id):
    question = get_object_or_404( Question, pk=question_id )

    return render(req, 'polls/results.html', { 'question': question })

def vote(req, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=req.POST['choice'])
    except( KeyError, Choice.DoesNotExist ):
        return render(req, 'polls/detail.html', {
            'question': question,
            'error_message': 'Please Make A Selection'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect( reverse( 'polls:results', args=(question.id, ) ) )