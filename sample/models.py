# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Employees(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    emp_id=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

