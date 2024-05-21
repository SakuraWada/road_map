from django.views import generic
from ..models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ..forms import RecruitmentForm
from django.shortcuts import redirect, render

@method_decorator(login_required, name="dispatch")
class PartyRecruitmentListView(generic.ListView):
    template_name = "overwin/party_recruitment_list.html"
    model = Recruitment

@method_decorator(login_required, name="dispatch")
class PartyRecruitmentCreateView(generic.CreateView):
    template_name = "overwin/party_recruitment_create.html"
    model = Recruitment
    form_class = RecruitmentForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)