from ..models import User
from ..forms.account_register_and_login import UserRegisterForm
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic
from django.utils.decorators import method_decorator

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
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)
        form = UserRegisterForm(instance=user)
        context = {
            'form': form,
        }
        return render(request, 'overwin/account_info_update.html', context)

@login_required
def delete_account(request):
    user = get_object_or_404(User, pk=request.user.pk)
    user.delete()
    return redirect(reverse('overwin:login'))

