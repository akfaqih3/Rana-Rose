from django.shortcuts import render
from Product.models import Product
from .models import CartProduct,Cart
from django.http.response import JsonResponse
import json

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/Account/login')
def addToCart(request):
    data = json.loads(request.body)
    user = request.user
    product_pk = data['pk']
    if user.is_authenticated :
        cart,create = Cart.objects.get_or_create(user=user,completed=False)
        product = Product.objects.get(pk=product_pk)
        cartProduct = CartProduct.objects.create(cart=cart,product=product)
        cart.refresh_from_db()
        cart_length = len(cart.products)
        pk_products = [product.pk for product in cart.products]

        the_cart=[]
        for pro in cart.products :
            the_cart.append(
                {
                    'pk':pro.pk,
                    'name':pro.name,
                    'desc':pro.description,
                    'price':pro.price,
                    'photo':pro.photo.url
                }
            )
    data_response={
         'pks':pk_products,
         'cart_total':cart.grand_total,
         'products':the_cart
    }
    return JsonResponse(data_response,safe=False)

@login_required(login_url='/Account')
def removeFromCart(request):
    data = json.loads(request.body)
    user = request.user
    product_pk = data['pk']
    if user.is_authenticated :
        cart,create = Cart.objects.get_or_create(user=user,completed=False)
        product = Product.objects.get(pk=product_pk)
        cartProduct = CartProduct.objects.get(cart=cart,product=product)
        CartProduct.delete(cartProduct)

        cart_length = len(cart.products)
        pk_products = [product.pk for product in cart.products]

        
        the_cart=[]
        for pro in cart.products :
            the_cart.append(
                {
                    'pk':pro.pk,
                    'name':pro.name,
                    'desc':pro.description,
                    'price':pro.price,
                    'photo':pro.photo.url
                }
            )
    data_response={
         'pks':pk_products,
         'cart_total':cart.grand_total,
         'products':the_cart
    }
    return JsonResponse(data_response,safe=False)