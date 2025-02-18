from django.http import JsonResponse


def site(request):
    site = {
        "pages": [
            {
                "children": [
                    {
                        "label": "Dashboard",
                        "url": "/",
                        "schemaApi": "/amis/",
                        "icon": "fa fa-home",
                        "iconPos": "left",
                        "isDefaultPage": True
                    }
                ]
            }
        ]
    }
    return JsonResponse(site)
