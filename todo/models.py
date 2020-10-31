from django.db import models
from django_extensions.db.models import TimeStampedModel
from .constants import COLORS, RED


class ToDo(TimeStampedModel):
    name = models.CharField(max_length=250, verbose_name='Nome')

    tags = models.ForeignKey('todo.Tag', on_delete=models.CASCADE)

    tasks = models.ForeignKey('todo.Task', on_delete=models.CASCADE)


class Tag(TimeStampedModel):
    name = models.CharField(max_length=250, verbose_name='Nome')

    color = models.CharField(max_length=10, choices=COLORS, default=RED)
    
    def __str__(self):
        return self.name


class Task(TimeStampedModel):
    name = models.CharField(max_length=250, verbose_name='Nome')
    
    def __str__(self):
        return self.name
