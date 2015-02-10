from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    message = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    topic = models.ForeignKey(Topic, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = "last_modified"


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    message = models.ForeignKey(Message)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = "creation_date"
