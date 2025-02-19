from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse


def index(request):
    index_json = {
        "type": "page",
        "body": [
            {
                "type": "calendar",
                "value": "NOW()",
                "todayActiveStyle": {
                    "backgroundColor": "#ef4444 !important",
                    "color": "#f8f9fa",
                    "border": "none",
                    "borderRadius": "15px"
                },
                "largeMode": True,
                "schedules": []
            }
        ]
    }
    return JsonResponse(index_json)


def helloworld(request):
    hello_json = {
        "type": "page",
        "initApi": "/api/helloworld/",
        "body": [
            {
                "type": "tpl",
                "tpl": "Hello ${text}!"
            }
        ]
    }
    return JsonResponse(hello_json)
