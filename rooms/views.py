from django.views.generic import ListView

from .models import RoomCategory

class HomePageView(ListView):
    model = RoomCategory
    template_name = 'home.html'
