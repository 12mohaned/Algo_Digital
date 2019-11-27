# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Algorthim_Category(models.Model):
    Category_name = models.CharField(max_length = 20, primary_key = True)
    Category_description = models.TextField()

    def __str__(self):
        return self.Category_name
            
class Algorthim(models.Model):
    Algorthim_id      = models.CharField(max_length = 30, primary_key = True)
    Algorthim_name    = models.TextField()
    Algorthim_Content = models.TextField()
    Algorthim_Code    = models.TextField()
    Category = models.ForeignKey(Algorthim_Category,verbose_name = "Category")

    def __str__ (self):
        return self.Algorthim_name
