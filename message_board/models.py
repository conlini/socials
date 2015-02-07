from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    text = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    topic = models.ForeignKey(Topic)
    creation_date = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    creation_date = models.DateTimeField(auto_now_add=True)