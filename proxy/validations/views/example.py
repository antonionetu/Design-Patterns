from .. import services
from django.http import JsonResponse


def example(request, user_id):
    data = services.example_proxy(request, user_id)

    return JsonResponse({
        'data': data
    })
