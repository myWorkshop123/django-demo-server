from django.http import HttpResponse

from django.http import JsonResponse

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    data = { "id": "1", "title": "iphone 9", "description": "some product", "price":"500", "views": 100 }
    response = JsonResponse(data, status=200)

    return response