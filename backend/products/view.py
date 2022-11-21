from django.http import JsonResponse, HttpResponse
import json
from . models import Product


"""
def api_test(request, *args, **kwargs):
    #print(request.body)
    #body = request.body
    print(request.body)
    data ={}
    try:
        data = json.loads(request.body)
    except:
        pass
    print(data)
    data['headers']=dict(request.headers)
    print(data['headers'])
    print("==============")
    # data['content_type'] = request.content_type
    # print(data['content_type'])
    print(request.GET)
    return JsonResponse(data)
"""

#django model instance as an API Response
"""
def api_test(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['content'] = model_data.content
        data['price'] = model_data.price
        return JsonResponse(data)
"""    

#Django model instance to Dictionary (with help of an import module👇👇👇)
from django.forms.models import model_to_dict
def api_test(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data = model_to_dict(model_data)
        return HttpResponse(data)