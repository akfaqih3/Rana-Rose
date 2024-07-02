from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils import timezone
from datetime import timedelta
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=128)
    photo = models.ImageField(upload_to='Categories/photos',blank=True,null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=128)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    photo = models.ImageField(upload_to='Products/photos/%y/%m/%d/',blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

class Offer(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    discount = models.IntegerField(validators=[MaxValueValidator(99.99),MinValueValidator(1.00)])
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.datetime.today)

    def __str__(self) -> str:
        return f"Offer for {self.product.name} (dicount: {self.discount}%)"
    
    def clean(self) -> None:
        if self.start_date and self.end_date and (self.start_date > self.end_date or self.start_date == self.end_date) :
            raise ValueError("Start date cannot be after or equal end date")