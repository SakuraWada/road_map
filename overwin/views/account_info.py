from ..models import User
from ..forms.account_register_and_login import AccountInfoUpdateForm
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator

@method_decorator(login_required, name="dispatch")
class AccountInfoView(generic.TemplateView):
    template_name = 'overwin/account_info/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        context['email'] = self.request.user.email
        return context

@method_decorator(login_required, name="dispatch")
class UpdateAccountInfoView(generic.UpdateView):
    template_name = 'overwin/account_info/update.html'
    model = User
    success_url = reverse_lazy('overwin:account_info')
    form_class = AccountInfoUpdateForm

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

    def get(self, request):
        self.object = self.get_object()
        form = self.get_form()
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.save()
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)

@method_decorator(login_required, name="dispatch")
class DeleteAccountInfoView(generic.DeleteView):
    model = User
    success_url = reverse_lazy('overwin:login')
    template_name = 'overwin/account_info/delete.html'

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

