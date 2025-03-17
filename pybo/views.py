from django.http import HttpResponse
from django.shortcuts import render

from pybo.models import Question

# Create your views here.

# http://127.0.0.1:8000/pybo/
def index(request):
    question_list = Question.objects.order_by("-create_date")
    context = {"question_list": question_list}
    return render(request, "pybo/question_list.html", context)

# http://127.0.0.1:8000/pybo/<int:question_id/>
def detail(request, question_id):
    question = Question.objects.get(id=question_id)

    context = {"question": question}
    return render(request, "pybo/question_detail.html", context)