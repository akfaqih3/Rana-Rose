from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import forms

# Create your views here.

class newAccount(FormView):
    form_class = forms.UserCreationForm
    template_name = 'registration/signup.html'
    success_url = 'Registration:login'