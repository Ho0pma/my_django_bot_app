from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)