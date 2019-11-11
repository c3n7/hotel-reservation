from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from rooms.models import RoomCategory

class RoomDashboardListView(ListView):
    model = RoomCategory
    template_name = 'roomdashboard_list.html'

class RoomDashboardDetailView(DetailView):
    model = RoomCategory
    template_name = 'roomdashboard_detail.html'

class RoomDashboardUpdateView(UpdateView):
    model = RoomCategory
    fields = ('category_name', 'summary', 'room_image', 'price', 'total_rooms')
    template_name = 'roomdashboard_edit.html'

class RoomDashboardDeleteView(DeleteView):
    model = RoomCategory
    template_name = 'roomdashboard_delete.html'
    success_url = reverse_lazy('roomdashboard_list')

class RoomDashboardCreateView(CreateView):
    model = RoomCategory
    fields = ('category_name', 'summary', 'room_image', 'price', 'total_rooms')
    template_name = 'roomdashboard_new.html'
    success_url = reverse_lazy('roomdashboard_list')
