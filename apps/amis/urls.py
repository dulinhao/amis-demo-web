from django.urls import path
from .views import *
from .site import site
urlpatterns = [
    path('', index, name='index'),
    path('site/', site, name='user'),
]