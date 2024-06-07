from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy,reverse
from django.shortcuts import render, get_object_or_404,redirect
from ..models import Recruitment, JoinMember
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
        applicated_to_recruiting = JoinMember.objects.filter(recruitment=recruitment, join_member=request.user).exists()
        possible_to_entry = recruitment.possible_to_entry
        form = RecruitmentForm(instance=recruitment)
        approved_message = None

        if is_owner:
            joined_members = JoinMember.objects.filter(recruitment=recruitment, is_approved=True)
            applicant_members = JoinMember.objects.filter(recruitment=recruitment, is_approved=False)
        else:
            joined_members = None
            applicant_members = None
            try:
                joined_member = JoinMember.objects.get(recruitment=recruitment, join_member=request.user, is_approved=True)
                approved_message = joined_member.message
            except JoinMember.DoesNotExist:
                pass

        context = {
            'recruitment': recruitment,
            'is_owner': is_owner,
            'applicated_to_recruiting' : applicated_to_recruiting,
            'possible_to_entry' : possible_to_entry,
            'form' : form,
            'joined_members': joined_members,
            'applicant_members': applicant_members,
            'approved_message': approved_message,
        }
        return render(request, 'overwin/party_recruitment_detail.html', context)

    def post(self, request, pk):
        recruitment = get_object_or_404(Recruitment, pk=pk)
        is_owner = request.user.pk == recruitment.owner.pk
        form = RecruitmentForm(instance=recruitment)

        # 募集者側の操作
        ## 募集の更新
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

        ## 参加申請の許可
        if 'approve_member' in request.POST:
            #NOTE: 許可ボタンが押された時に、そのユーザーのIDを取得
            member_id = request.POST.get('member_id')
            message = request.POST.get('message')
            if member_id and message:
                try:
                    join_member = JoinMember.objects.get(recruitment=recruitment, join_member__id=member_id, is_approved=False)
                    join_member.is_approved = True
                    join_member.message = message
                    join_member.save()
                    recruitment.current_member_count += 1
                    recruitment.save()
                except JoinMember.DoesNotExist:
                    pass
            return redirect('overwin:party_recruitment_detail', pk=pk)

        # 参加者側の操作
        if 'join' in request.POST:
            # 未申請の場合は参加申請ができる
            if not JoinMember.objects.filter(recruitment=recruitment, join_member=request.user).exists():
                JoinMember.objects.create(recruitment=recruitment, join_member=request.user)
                return redirect('overwin:party_recruitment_detail', pk=pk)

        context = {
            'recruitment': recruitment,
            'is_owner': is_owner,
            'form' : form
        }
        return render(request, 'overwin/party_recruitment_detail.html', context)

@method_decorator(login_required, name="dispatch")
class PartyRecruitmentUpdateView(generic.UpdateView):
    template_name = 'overwin/party_recruitment_update.html'
    model = Recruitment
    form_class = RecruitmentForm

    def get_success_url(self):
        return reverse("overwin:party_recruitment_detail", kwargs={'pk': self.object.pk})

@method_decorator(login_required, name="dispatch")
class PartyRecruitmentDeleteView(generic.DeleteView):
    model = Recruitment
    success_url = reverse_lazy('overwin:party_recruitment_list')
    template_name = 'overwin/party_recruitment_delete.html'
