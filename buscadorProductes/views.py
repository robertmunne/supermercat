# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from buscadorProductes.models import Producto


# Create your views here.
def search(request):
    return render(request, "buscadorProductes/search.html")


def login(request):
    return render(request, "buscadorProductes/login.html")


def home(request):
    return render(request, "buscadorProductes/home.html")
