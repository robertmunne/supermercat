from django.conf.urls import url
from .views import search
from .views import login
from .views import home

urlpatterns = [
    url(r'search$', search),
    url(r'login$', login),
    url(r'^$', home),

]
