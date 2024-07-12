from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Product,Category,Offer
from django.core.paginator import Paginator
from datetime import datetime

from Cart.utils import Cart
# Create your views here.

class ProductDetails(DetailView):
    model = Product
    template_name = 'product/details.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        releaseProducts = Product.objects.filter(category=self.get_object().category)
        object = Product.objects.get(pk=self.kwargs['pk'])
        offer = object.offer_set.filter(end_date__gte=datetime.today()).last()

        cart = Cart(self.request).get()
        context = {
            'releaseProducts':releaseProducts,
            'object':object,
            'offer':offer,
            'cart':cart
        }
        return context

class List(ListView):
    model = Product
    template_name = 'product/list.html'
    def get_queryset(self) -> QuerySet[Any]:
        category = Category.objects.get(name=self.kwargs['category'])
        objects = Product.objects.filter(category=category)
        return objects.all()
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        name = self.kwargs['category']
        categories = Category.objects.all()
        object_list = self.get_queryset()
        pages = Paginator(object_list,12)
        page = pages.get_page(self.request.GET.get('page'))

        cart = Cart(self.request).get()

        context = {
            'category_name':name,
            'categories' : categories,
            'page':page,
            'cart':cart
        }
        return context