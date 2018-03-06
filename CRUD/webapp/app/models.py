# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class student_table(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    section = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    marks = models.IntegerField(default=0)
    
