from django.db import models
from django.contrib.auth.models import User
from Product.models import Product
from django.utils.timezone import datetime
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    @property
    def grand_total(self):
        products = self.CartProduct_set.all()
        total = sum([product.price for product in products])
        return total

    @property
    def products(self):
        products = [product.product for product in self.cartproduct_set.all()]
        return products
    
    def __str__(self) -> str:
        return f"{self.user}    {self.completed}"
    
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    added_at = models.DateTimeField(auto_now=True)

    @property
    def net_price(self):
        product = self.product
        if product.Offer_set :
            offer = product.Offer_set.filter(end_date__gte=datetime.today()).last()
            if offer:
                #price = (product.price * (100 - offer.discount))/100 
                return offer.net_price
            
        return product.price 
    
    def __str__(self) -> str:
        return f"{self.product.pk}    {self.product.name}   {self.cart.user}"
        