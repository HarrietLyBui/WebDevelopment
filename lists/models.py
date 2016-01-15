from __future__ import unicode_literals

from django.db import models
class List(models.Model):
    name = models.TextField(default='') #tell Django we have an item text and it contains string of data


class Item(models.Model):
    text = models.TextField(default='') #tell Django we have an item text and it contains string of data
    list = models.ForeignKey(List, default=None)
    is_done = models.BooleanField(default=False)
