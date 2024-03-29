from email.policy import default

#from django
from django.db import models


class Product(models.Model):
    """"
    name: Product
    description: This class keep records about a particular Product.
    """
    title   = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    price   = models.DecimalField(max_digits =15, decimal_places=2, default=99.99 )
    
    def __str__(self):
        return self.title
    
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)
    
    def get_discount(self):
        return "2500"
