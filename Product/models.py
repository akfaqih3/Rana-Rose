from django.db import models

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