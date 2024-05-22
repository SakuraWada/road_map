from ..models import *
from ..forms import *
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator

#クラスベースビューだとurlにslugやpkが必要になるので関数ビューで実装
@login_required
def show_account_info(request):
    user = get_object_or_404(User, pk=request.user.pk)
    context = {
        'username': user.username,
        'email': user.email,
    }
    return render(request, 'overwin/account_info.html', context)

@method_decorator(login_required, name="dispatch")
class UpdateAccountInfoView(generic.UpdateView):
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

@login_required
def delete_account(request):
    user = get_object_or_404(User, pk=request.user.pk)
    user.delete()
    return redirect(reverse('overwin:login'))

