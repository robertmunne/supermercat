from django.conf.urls import url
from django.contrib import admin

from .views import search
from .views import login
from .views import home

urlpatterns = [
    url(r'search$', search),
    url(r'login$', login),
    url(r'^$', home),
    url(r'home$', home),
]
