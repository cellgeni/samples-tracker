from django.db import models


class Action(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Stage(models.Model):
    action = models.ForeignKey(Action, null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return str(self.action) + " " + str(self.date)


class Sample(models.Model):
    sid = models.CharField(max_length=100)
    stages = models.ManyToManyField(Stage)

    def __str__(self):
        return str(self.sid)
