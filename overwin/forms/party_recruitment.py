from django import forms
from ..forms_utils import CustomForm
from ..models import Recruitment

class RecruitmentForm(CustomForm, forms.ModelForm):
    class Meta:
        model = Recruitment
        fields = ['max_recruit_member', 'comment']