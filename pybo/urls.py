from django.contrib import admin
from django.urls import include, path
from pybo import views

## http://127.0.0.1:8000/pybo
urlpatterns = [
    path("", views.index),
    path("<int:question_id>/", views.detail), # /3
]
