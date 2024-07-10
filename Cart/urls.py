from django.urls import path
from . import views


app_name = 'Cart'

urlpatterns = [
    path('addToCart/',views.addToCart,name='addToCart'),
    path('removeFromCart/',views.removeFromCart,name='removeFromCart'),
]