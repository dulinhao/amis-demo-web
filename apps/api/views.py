from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


# Create your views here.

def helloworld(request):
    return JsonResponse(
        {
            "code": 0,
            "msg": "success",
            "data": {
                "text": "World!"
            }
        }
    )
