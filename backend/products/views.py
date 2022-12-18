#from rest_framework
from rest_framework import serializers
from rest_framework import status, generics, mixins, permissions, authentication

from rest_framework.response import Response
from rest_framework.decorators import api_view

#from django
from django.http import Http404
from django.shortcuts import get_object_or_404

#from project
from . models import Product
from . serializers import ProductSerializer


#ClassBasedView 👇👇👇
#for Listing
class ProductListAPIView(generics.ListAPIView):
    """
    Name: ProductListAPIView
    Description: Since i can transform the CreateAPIView to ListCreateAPIView
    then in the test file  i can used the requests.get() for ListAPIView (in the list.py file)&
     request.post() for CreateAPIView (in the create.py file)
   """
    queryset          = Product.objects.all()
    serializer_class  = ProductSerializer
    
product_list_view = ProductListAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset         = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes  = [permissions.IsAuthenticated]
    #lookup_field = 'pk' ??
    
#To create or list    
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset                = Product.objects.all()
    serializer_class        = ProductSerializer
    authentication_classes  = [authentication.SessionAuthentication]
    permission_classes      = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
       
        #serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title    = serializer.validated_data.get('title')
        content  = serializer.validated_data.get('content'), None
        if content is None:
            content = title            
        serializer.save(content=content)
        #or you can send a django signal 
    
product_list_create_view  = ProductListCreateAPIView.as_view()

#To Update
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset         = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
  
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
             
            
product_update_view = ProductUpdateAPIView.as_view()

#To Delete-->Up
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset         = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)
    
product_delete_view = ProductDestroyAPIView.as_view()


#Mixins and a GenericAPIView
class ProductMixinView(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       generics.GenericAPIView):
    queryset          = Product.objects.all()
    serializer_class  = ProductSerializer
    lookup_field      = 'pk'
    
    def get(self, request, *args, **kwargs):  #HTTP---> get  
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs): #HTTP--->post
             return self.create(request, *args, **kwargs)
    
product_mixins_view = ProductMixinView.as_view()

    #def post() #HTTP---> post


#functionBasedView 👇👇👇
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            #url_args
            #get request--> detail view
            obj  = get_object_or_404(Product, pk=pk)       # queryset = Product.objects.filter(pk=pk)
            data = ProductSerializer(obj, many=False).data # if not queryset.exist():
            return Response(data)                          #     raise Http404
                                                           # return Response()
        #get request--> list view
        queryset = Product.objects.all()
        data     = ProductSerializer(queryset, many=True).data
        return Response(data)
    
    if method == "POST":
        #create item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            #instance = serializer.save()
            title    = serializer.validated_data.get('title')
            content  = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
       
        return Response({"Invalid": "Not Good Data"}, status=status.HTTP_406_NOT_ACCEPTABLE)
