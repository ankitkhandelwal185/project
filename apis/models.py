# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    headline = models.CharField(max_length=100)
    content = models.CharField(max_length=300)

    def __str__(self):
        return self.headline