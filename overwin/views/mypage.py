from django.views import generic

class MyPageView(generic.TemplateView):
    template_name = "overwin/mypage/mypage.html"