# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Algorthim ,Algorthim_Category
class AlgorthimAdmin(admin.ModelAdmin):
    fields = ["Algorthim_id","Algorthim_name","Algorthim_Content","Algorthim_Code","Category"]
admin.site.register(Algorthim,AlgorthimAdmin)

class CategoryAdmin(admin.ModelAdmin):
    fields = ["Category_name", "Category_description"]
admin.site.register(Algorthim_Category,CategoryAdmin)
# Register your models here.
