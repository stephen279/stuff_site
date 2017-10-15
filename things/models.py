from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Thing(models.Model):
    created_At = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    move_number = models.IntegerField()

    def __str__(self):
        return self.title



class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    thing = models.ForeignKey(Thing)
    content = models.TextField(blank=True)
    number_increment = models.IntegerField()

    def __str__(self):
        return self.title

    class meta:
        ordering = ['order']
