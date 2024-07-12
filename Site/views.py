from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView,ListView
# Create your views here.
from Product.models import Product,Category,Offer
from Cart.models import Cart
from datetime import datetime
from Cart.utils import Cart
class Home(TemplateView):
    template_name='base.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        products = Product.objects.all()
        categories = Category.objects.all()
        carousels = Product.objects.order_by('-pk')[:3]
        offers = Offer.objects.filter(end_date__gte=datetime.today())

        cart = Cart(self.request).get()
        context = {
            'products':products,
            'categories':categories,
            'carousels':carousels,
            'offers':offers,
            'cart':cart,
        }
        return context