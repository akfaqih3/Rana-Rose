from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView ,FormView
from .forms import SignupForm
from django.contrib.auth.views import PasswordResetView
# Create your views here.

class newAccount(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    
    def dispatch(self, request: HttpRequest) -> HttpResponse:
        if self.request.user.is_authenticated :
            return redirect('Site:Home')
    
    def get_success_url(self) -> str:
        return reverse_lazy('Registration:login')
    

class ResetPassword(PasswordResetView):
    template_name = "registration/password_reset_form.html"
    email_template_name = "registration/password_reset_email.html"
    subject_template_name = "registration/password_reset_subject.txt"
    