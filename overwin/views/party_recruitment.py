from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from ..models import Recruitment, JoinedMember
from ..forms.party_recruitment import RecruitmentForm

@method_decorator(login_required, name="dispatch")
class RecruitmentListView(generic.ListView):
    model = Recruitment
    template_name = 'overwin/party_recruitment_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_recruitment']   = Recruitment.objects.filter(owner=self.request.user)
        context['other_recruitments'] = Recruitment.objects.exclude(owner=self.request.user)
        return context

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
        applicated_to_recruiting = JoinedMember.objects.filter(recruitment=recruitment, join_member=request.user).exists()
        has_full_member = recruitment.current_member_count >= recruitment.max_recruit_member
        form = RecruitmentForm(instance=recruitment)
        context = {
            'recruitment': recruitment,
            'is_owner': is_owner,
            'applicated_to_recruiting' : applicated_to_recruiting,
            'has_full_member' : has_full_member,
            'form' : form,
        }
        return render(request, 'overwin/party_recruitment_detail.html', context)

    def post(self, request, pk):
        recruitment = get_object_or_404(Recruitment, pk=pk)
        is_owner = request.user.pk == recruitment.owner.pk
        form = RecruitmentForm(instance=recruitment)

        #募集者側の操作
        if 'recruitment_update' in request.POST:
            if form.is_valid():
                form.save()
                return redirect('overwin:party_recruitment_detail', pk=pk)
            else:
                context = {
                    'recruitment': recruitment,
                    'is_owner': is_owner,
                    'form': form,
                    'error_message': 'フォームが無効です。',
                }
                return render(request, 'overwin/party_recruitment_detail.html', context)

        #参加者側の操作
        if 'join' in request.POST:
            # 既に参加申請済みの場合は何もしない
            if JoinedMember.objects.filter(recruitment=recruitment, join_member=request.user).exists():
                pass
            # 募集に未申請の場合は参加申請ができる
            else:
                JoinedMember.objects.create(recruitment=recruitment, join_member=request.user)
                recruitment.current_member_count += 1
                recruitment.save()
                return redirect('overwin:party_recruitment_detail', pk=pk)

        context = {
            'recruitment': recruitment,
            'is_owner': is_owner,
            'form' : form
        }
        return render(request, 'overwin/party_recruitment_detail.html', context)

@method_decorator(login_required, name="dispatch")
class PartyRecruitmentDeleteView(generic.DeleteView):
    model = Recruitment
    success_url = reverse_lazy('overwin:party_recruitment_list')
    template_name = 'overwin/recruitment_delete.html'
