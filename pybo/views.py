from django.http import HttpResponse
from django.shortcuts import render

from pybo.models import Question

# Create your views here.

# http://127.0.0.1:8000/hello/


def index(request):
    # Question 모델의 데이터를 create_date 기준으로 내림차순 정렬하여 가져오는 것
    question_list = Question.objects.order_by("-create_date")
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)