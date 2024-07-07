from django.db import models

from django.contrib.auth.models import User
from Product.models import Product
from django.utils import timezone
# Create your models here.

class OrderStatus(models.Choices):
    onDemand = 'onDemand'
    onDelivery = 'onDelivery'
    recieved = 'recieved'

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=16,choices=OrderStatus.choices)
    products = models.ManyToManyField(Product)