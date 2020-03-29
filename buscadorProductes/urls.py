from django.conf.urls import url
from django.contrib import admin

from .views import search
from .views import login_view
from .views import home
from .views import register

urlpatterns = [
    url(r'search$', search),
    url(r'login_view$', login_view),
    url(r'register$', register),
    url(r'^$', home),
    url(r'home$', home),
]
