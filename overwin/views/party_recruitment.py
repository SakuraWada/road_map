from django.views import generic
from ..models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ..forms import RecruitmentForm
from django.urls import reverse_lazy

@method_decorator(login_required, name="dispatch")
class PartyRecruitmentListView(generic.ListView):
    template_name = "overwin/party_recruitment_list.html"
    model = Recruitment

@method_decorator(login_required, name="dispatch")
class PartyRecruitmentCreateView(generic.CreateView):
    template_name = "overwin/party_recruitment_create.html"
    model = Recruitment
    form_class = RecruitmentForm
    success_url = reverse_lazy("overwin:party_recruitment_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)