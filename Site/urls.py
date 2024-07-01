from django.urls import path 
from . import views

app_name = 'Site'

urlpatterns = [
    path('',views.Home.as_view(),name='Home')
]