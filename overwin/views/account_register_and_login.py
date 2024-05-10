from django.contrib.auth import login,authenticate
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.views import generic
from django.urls import reverse_lazy
from ..forms import *

class AccountRegisterView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = "overwin/account_register.html"
    success_url = reverse_lazy("overwin:login")

    def form_valid(self, form):
        response = super().form_valid(form)
        password = form.cleaned_data.get("password")
        username = form.cleaned_data.get("username")
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response

class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = "overwin/login.html"

class LogoutView(BaseLogoutView):
    success_url = reverse_lazy('overwin:login')

