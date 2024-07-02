from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView,ListView
# Create your views here.
from Product.models import Product,Category

class Home(TemplateView):
    template_name='base.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        products = Product.objects.all()
        categories = Category.objects.all()
        carousel = Product.objects.all()[:3]
        context = {
            'products':products,
            'categories':categories,
            'carousels':carousel
        }
        return context