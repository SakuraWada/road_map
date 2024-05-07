from django.views import generic
from ..models import *

class PlayerSearchView(generic.ListView):
    model = Player
    template_name = "overwin/search_player.html"