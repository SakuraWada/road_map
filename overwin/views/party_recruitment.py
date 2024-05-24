from django.views import generic
from ..models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ..forms import *
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404,redirect

@login_required
def show_recruitement_list(request):
    user_recruitment = Recruitment.objects.filter(owner=request.user)
    other_recruitments = Recruitment.objects.exclude(owner=request.user)
    context = {
        'user_recruitment': user_recruitment,
        'other_recruitments': other_recruitments,
    }
    return render(request, 'overwin/party_recruitment_list.html', context)

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
        form = RecruitmentForm(instance=recruitment)
        context = {
            'recruitment': recruitment,
            'is_owner': is_owner,
            'form' : form
        }
        return render(request, 'overwin/party_recruitment_detail.html', context)
