from django.urls import path
from . import views
app_name = 'Product'
urlpatterns = [
    path('<int:pk>',views.ProductDetails.as_view(),name='productDetails'),
    path('<str:category>',views.List.as_view(),name='list')
]