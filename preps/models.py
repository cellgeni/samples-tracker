from django.db import models
from django.utils import timezone


class Action(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Sample(models.Model):
    sid = models.CharField(max_length=100)

    def __str__(self):
        return str(self.sid)


class Stage(models.Model):
    action = models.ForeignKey(Action, null=True, blank=True, on_delete=models.SET_NULL)
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    active = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return str(self.action) + " " + str(self.date) + " " + str(self.sample)