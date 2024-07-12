from django.urls import path 
from . import views

app_name = 'Order'

urlpatterns=[
    path('',views.Checkout.as_view(),name='checkout'),
]