import copy
from rest_framework import serializers
from . models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    interest = copy.copy(my_discount)
    class Meta:
        model   = Product
        fields  = [
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
            'interest'
        ]
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
    
    def get_interest(self, obj):
        return '5000'