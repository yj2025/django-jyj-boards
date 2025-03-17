from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from django.utils import timezone
from pybo.models import Answer, Question

# Create your views here.

# http://127.0.0.1:8000/pybo/
def index(request):
    question_list = Question.objects.order_by("-create_date")
    context = {"question_list": question_list}
    return render(request, "pybo/question_list.html", context)

# http://127.0.0.1:8000/pybo/<int:question_id/>
def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "pybo/question_detail.html", context)

# dev_5
def answer_create(request, question_id):
    # answer/create/6/
    question = get_object_or_404(Question, pk=question_id)

    content = request.POST.get("content")

    # select * from question, answer where answer.question_id = 6
    # question.answer_set.create(content=content, create_date=timezone.now())
    
    answer = Answer(question=question, content=content, create_date=timezone.now())
    answer.save()

    return redirect('pybo:detail', question_id=question_id)

