from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# http://127.0.0.1:8000/hello/


def index(request):
    return HttpResponse("<h1>안녕하세요.</h1> </br>게시판을 만들겠습니다.")


def hello(request):
    return HttpResponse("<h1>홍길동 입니다.</h1>")