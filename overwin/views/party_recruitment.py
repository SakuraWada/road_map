from django.views import generic
from ..models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ..forms import RecruitmentForm,RecruitmentUpdateForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404,redirect

@method_decorator(login_required, name="dispatch")
class RecruitmentListView(generic.ListView):
    model = Recruitment
    template_name = 'overwin/party_recruitment_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_recruitment']   = Recruitment.objects.filter(owner=self.request.user)
        context['other_recruitments'] = Recruitment.objects.exclude(owner=self.request.user)
        # breakpoint()
        return context

# @login_required
# def show_recruitement_list(request):
#     user_recruitment = Recruitment.objects.filter(owner=request.user)
#     other_recruitments = Recruitment.objects.exclude(owner=request.user)
#     context = {
#         'user_recruitment': user_recruitment,
#         'other_recruitments': other_recruitments,
#     }
#     return render(request, 'overwin/party_recruitment_list.html', context)

@method_decorator(login_required, name="dispatch")
class PartyRecruitmentCreateView(generic.CreateView):
    template_name = "overwin/party_recruitment_create.html"
    model = Recruitment
    form_class = RecruitmentForm
    success_url = reverse_lazy("overwin:party_recruitment_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name="dispatch")
class PartyRecruitmentDetailView(generic.DetailView):
    def get(self, request, pk):
        recruitment = get_object_or_404(Recruitment, pk=pk)
        is_owner = request.user.pk == recruitment.owner.pk
        form = RecruitmentUpdateForm(instance=recruitment)
        context = {
            'recruitment': recruitment,
            'is_owner': is_owner,
            'form' : form
        }
        return render(request, 'overwin/party_recruitment_detail.html', context)

    def post(self, request, pk):
        recruitment = get_object_or_404(Recruitment, pk=pk)
        is_owner = request.user.pk == recruitment.owner.pk
        form = RecruitmentUpdateForm(instance=recruitment)
        context = {
            'recruitment': recruitment,
            'is_owner': is_owner,
            'form' : form
        }
        return render(request, 'overwin/party_recruitment_detail.html', context)

# @login_required
# def recruitment_delete(request):
#     recruitment = get_object_or_404(Recruitment, owner=request.user)
#     recruitment.delete()
#     return redirect(reverse('overwin:login'))

# @login_required
# def recruitment_join(request, pk):
#     # 他人の募集に参加
#     recruitment = get_object_or_404(Recruitment, pk=pk)
#     # 参加処理...