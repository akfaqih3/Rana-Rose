from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from Cart.utils import Cart

class Checkout(TemplateView):
    template_name = 'Order/checkout.html'

    def get_context_data(self):
        cart = Cart(self.request).get()
        context = {
            'cart':cart
        }
        return context