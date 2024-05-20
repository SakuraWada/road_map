from django.views import generic
from ..models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name="dispatch")
class PartyRecruitmentListView(generic.ListView):
    template_name = "overwin/party_recruitment.html"