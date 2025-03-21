from django.db import models

# Create your models here.


# dev_2
# 하나의 질문에 다수의 답변 등록가능
class Question(models.Model):
    subject = models.CharField(max_length=100)  # 제목
    content = models.TextField()  # 글자 수 제한이 없는 텍스트 = TextField
    create_date = models.DateTimeField()  # 작성일시

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    content = models.TextField()
    create_date = models.DateTimeField()


# q=Question.objects.get(id=4)
# q.answer_set.all()
# <QuerySet [<Answer: Answer object (3)>, <Answer: Answer object (4)>, <Answer: Answer object (8)>]>

# .answer_set.all()    # 4.answer_set.all() # 역방향 참조
# Question .answers.all()    # 4.answers.all() # 역방향 참조
