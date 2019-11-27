# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Algorthim, Algorthim_Category
def home(request):
    if(request.path != "/Home"):
        return HttpResponse("Sorry this page is not here")

    else:
        return render(request =request,template_name = "Algorthims/base.html")

def Searching(request):
    if(request.path != "/SearchingAlgorthims/"):
        return HttpResponse("Sorry this page is not here" + request.path)

    else:
        return render(request =request,template_name = "Algorthims/Searching.html",
        context = {"SearchingAlgorthims" : Algorthim.objects.filter(Category = "Searching")})

def SearchingAlgorthims(request, algo):
    Choosen_Algorithm = Algorthim.objects.get(Algorthim_id = algo)

    return render(request,template_name ="Algorthims/Searching.html",context = {"Choosen" : Choosen_Algorithm})
