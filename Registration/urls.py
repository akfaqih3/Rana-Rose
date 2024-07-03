from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name='Registration'

urlpatterns=[
    path('login/',auth_views.LoginView.as_view(next_page='Site:Home'),name='login'),
    path('signup/',views.newAccount.as_view(),name='signup'),
    path('logout/',auth_views.LogoutView.as_view(next_page='Site:Home'),name='logout')
]