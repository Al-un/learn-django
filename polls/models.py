from django.db import models


class Poll(models.Model):
    topic = models.CharField(max_length=200)
    public = models.BooleanField(default=True)
    closed = models.BooleanField(default=False)


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
