# Create your models here.
from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    time = models.CharField(max_length=50)
    notes = models.TextField()
    score = models.IntegerField()
    submission = models.BooleanField()

    def __str__(self):
        return self.task_name
