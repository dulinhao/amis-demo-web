from django.urls import path
from .views import *
urlpatterns = [
    path('helloworld/', helloworld, name='helloworld'),
]