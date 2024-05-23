from ..models import User
from ..forms.account_register_and_login import UserRegisterForm
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator

@method_decorator(login_required, name="dispatch")
class AccountInfoView(generic.TemplateView):
    template_name = 'overwin/account_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        context['email'] = self.request.user.email
        return context

@method_decorator(login_required, name="dispatch")
class UpdateAccountInfoView(generic.UpdateView):
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)
        form = UserRegisterForm(instance=user)
        context = {
            'form': form,
        }
        return render(request, 'overwin/account_info_update.html', context)

@method_decorator(login_required, name="dispatch")
class DeleteAccountInfoView(generic.DeleteView):
    model = User
    success_url = reverse_lazy('overwin:login')
    template_name = 'overwin/account_delete.html'

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

