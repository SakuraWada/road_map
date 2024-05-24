from django.views import generic
from ..models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

@method_decorator(login_required, name="dispatch")
class FavoritePlayerView(generic.ListView):
    template_name = "overwin/favorite_game_player.html"
    model = FavoriteGamePlayer
    query_set = FavoriteGamePlayer.objects.all()

    def post(self, request, *args, **kwargs):
        favorite_id = request.POST.get('favorite_id')
        if favorite_id:
            favorite = FavoriteGamePlayer.objects.get(id=favorite_id, user=request.user)
            favorite.delete()
        return redirect('overwin:favorite_game_player')