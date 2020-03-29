# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
from buscadorProductes.models import Producto


# Create your views here.
def search(request):
    return render(request, "buscadorProductes/search.html",
                  {'nproductos': Producto.objects.count()})


def login_view(request):
    user = None
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...•••••••••
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)
        # else:
        # return render(request, "buscadorProductes/register.html", {'form': form})

        # Si existe un usuario con ese nombre y contraseña
        if user is not None:
            # Hacemos el login manualmente
            do_login(request, user)
            # Y le redireccionamos a la portada
            return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "buscadorProductes/login_view.html", {'form': form})

    # return render(request, "buscadorProductes/login.html")


def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "buscadorProductes/register.html", {'form': form})


def home(request):
    return render(request, "buscadorProductes/home.html")
