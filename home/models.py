from django.db import models
from django.contrib.auth.models import User
class Person(models.Model):
    name = models.CharField(max_length=32,default='amir')
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name



class Question(models.Model):
    User = models.ForeignKey(User,verbose_name='کاربر مورد نظر', on_delete=models.CASCADE, related_name='userquestion')
    title = models.CharField(max_length=24,verbose_name='عنوان سوال')
    slug = models.SlugField(max_length=24)
    body = models.CharField(max_length=120)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.User} - {self.title} - {self.body[:20]}"


class Answer(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE, related_name='useranswer')
    whitch_question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='whitch_answer')
    bode = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.User} - {self.whitch_question.title[:20]}"
