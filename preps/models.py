from django.db import models


class Action(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Stage(models.Model):
    actions = models.ManyToManyField(Action)
    name = models.CharField(max_length=200)
    date = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return str(self.name)


class Sample(models.Model):
    sid = models.CharField(max_length=100)
    stages = models.ManyToManyField(Stage)

    def __str__(self):
        return str(self.sid)
