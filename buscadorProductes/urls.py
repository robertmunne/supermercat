from django.conf.urls import url
from django.contrib import admin

from .views import search
from .views import login_view
from .views import home
<<<<<<< HEAD
from .views import register
=======
from .views import productes
>>>>>>> jorge

urlpatterns = [
    url(r'search$', search),
    url(r'login_view$', login_view),
    url(r'register$', register),
    url(r'^$', home),
    url(r'home$', home),
    url(r'productes$', productes),
]
