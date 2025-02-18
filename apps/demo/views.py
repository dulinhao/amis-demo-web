from django.shortcuts import render
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'home.html')


def ping(request):
    return JsonResponse({"status": 0, "msg": "pong"})

