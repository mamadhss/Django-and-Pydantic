from enum import unique
from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=512,unique=True)
    content = models.TextField()

    def __str__(self):
        return f'{self.author}: {self.title}'


