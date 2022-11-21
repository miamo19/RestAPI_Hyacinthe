from django.http import JsonResponse
import json

#Create your views here.
def api_home(request, *args, **kwargs):
    body = request.body  #byte string of JSON data
    print(type(body))
    print(request.GET)   # url query params
    data = {}
    try:
        data = json.loads(body)  #take a string of JSON data ---> turn it to Python dictionary
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)  #converti to a dictinary but it's already a dictionary
    print(data['params'])

    data['headers'] = request.headers   #request.META -->   (this cannot automaticaly convert to JSON)
    print(data['headers'])

    json.dumps(dict(data['headers']))
    data['content_type'] = request.content_type
    return JsonResponse({"message": "Hi there, This is your django API crash course", "name":"Hyacinth", "Age": 18})


#block of views.py code commented (functionbased view)
"""
from urllib import response
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse


from . models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


# Create your views here.
@api_view(['POST'])
def api_home2(request, *args, **kwargs):
    
    serializer = ProductSerializer(data=request.data) #create item
    if serializer.is_valid(raise_exception=True):
        #instance = serializer.save()
        print(serializer.data)
        data = serializer.data
        return Response(data)
    return Response({"Invalid": "Not Good Data"}, status=400)
    
"""