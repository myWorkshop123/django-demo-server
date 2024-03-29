from django.http import Http404
from .models import Product
from django.http import JsonResponse
import request

def detail(request, poll_id):
    try:
        base_url = 'https://www.someprivateapi.com/search?'
        response = request.get(base_url + poll_id)
        
        p = Product.objects.get(pk=poll_id)
        data = { "id": p.pk, "title": p.title, "description": p.description, "price": p.price}
    except Product.DoesNotExist:
        raise Http404("Poll does not exist")
    return JsonResponse(data, status=200)
