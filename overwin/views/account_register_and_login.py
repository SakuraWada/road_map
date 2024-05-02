from django.contrib.auth import login,authenticate
from django.views import generic
from django.template import loader
from django.urls import reverse_lazy
from ..forms import UserRegisterForm

class AccountRegisterView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = "overwin/account_register.html"
    success_url = reverse_lazy("overwin:mypage")

    def form_valid(self, form):
        response = super().form_valid(form)
        password = form.cleaned_data.get("password")
        username = form.cleaned_data.get("username")
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response

