from ..models import *
from ..forms import *
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

#クラスベースビューだとurlにslugやpkが必要になるので関数ビューで実装
@login_required
def show_account_info(request):
    user = get_object_or_404(User, pk=request.user.pk)
    context = {
        'username': user.username,
        'email': user.email,
    }
    return render(request, 'overwin/account_info.html', context)

@login_required
def update_account_info(request):
    user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = AccountInfoUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse('overwin:account_info'))
    else:
        form = AccountInfoUpdateForm(instance=user)
        context = {
            'form': form,
        }
    return render(request, 'overwin/account_info_update.html', context)