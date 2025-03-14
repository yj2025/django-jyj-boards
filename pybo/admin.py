from atexit import register
from django.contrib import admin

from pybo.models import Question

# from pybo.models import Question
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ["subject", "content"]

admin.site.register(Question, QuestionAdmin)
