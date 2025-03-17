from django.contrib import admin
from django.urls import include, path
from pybo import views

app_name = "pybo"

## http://127.0.0.1:8000/pybo
urlpatterns = [
    path("", views.index, name='index'),
    ## http://127.0.0.1:8000/pybo/<int:question_id>/
    path("<int:question_id>/", views.detail, name="detail"), # /3
    path("answer/create/<int:question_id>/", views.answer_create, name="answer_create"), # dev_5
]
