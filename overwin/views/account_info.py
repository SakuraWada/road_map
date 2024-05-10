from django.views import generic
from ..models import *
from ..forms import *
from django.urls import reverse

class AccountInfoView(generic.DetailView):
    model=User
    template_name = "overwin/account_info.html"
    slug_field = 'slug'
    slug_url_kwarg = 'account_info'

class AccountInfoUpdateView(generic.UpdateView):
    model = User
    form_class = AccountInfoUpdateForm
    template_name = 'overwin/account_info_update.html'
    slug_field = 'slug'
    slug_url_kwarg = 'account_info'
    def get_success_url(self):
        url = reverse('overwin:account_info')
        return url