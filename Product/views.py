from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Product,Category,Offer
from django.core.paginator import Paginator
from datetime import datetime
# Create your views here.

class ProductDetails(DetailView):
    model = Product
    template_name = 'product/details.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        releaseProducts = Product.objects.filter(category=self.get_object().category)
        object = Product.objects.get(pk=self.kwargs['pk'])
        context = {
            'releaseProducts':releaseProducts,
            'object':object
        }
        return context
    
class OfferDetails(DetailView):
    model = Offer
    template_name = 'product/details.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        releaseProducts = Offer.objects.filter(end_date__gte=datetime.today())
        object = Offer.objects.get(pk=self.kwargs['pk'])
        context = {
            'releaseProducts':releaseProducts,
            'object':object
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
        context = {
            'category_name':name,
            'categories' : categories,
            'page':page
        }
        return context