#from django
from django import forms

#from prject
from . models import Product

class ProductForm(forms.ModelForm):
    """
    name: ProductForm
    description: This class gives point of a form to be filled
    """
    class Meta:
        model   = Product
        fields  = [
            'title',
            'content',
            'price'
        ]
