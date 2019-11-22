from braces.views import (
    LoginRequiredMixin,
    SuperuserRequiredMixin,
)

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from rooms.models import RoomCategory
from bookedrooms.models import BookedRoom

class RoomDashboardListView(LoginRequiredMixin, SuperuserRequiredMixin, ListView):
    model = RoomCategory
    template_name = 'roomdashboard_list.html'
    login_url = 'login'

class RoomDashboardDetailView(LoginRequiredMixin, SuperuserRequiredMixin, DetailView):
    model = RoomCategory
    template_name = 'roomdashboard_detail.html'
    login_url = 'login'

class RoomDashboardUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    model = RoomCategory
    fields = ('category_name', 'summary', 'room_image', 'price', 'total_rooms')
    template_name = 'roomdashboard_edit.html'
    login_url = 'login'

class RoomDashboardDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, DeleteView):
    model = RoomCategory
    template_name = 'roomdashboard_delete.html'
    success_url = reverse_lazy('roomdashboard_list')
    login_url = 'login'

class RoomDashboardCreateView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    model = RoomCategory
    fields = ('category_name', 'summary', 'room_image', 'price', 'total_rooms')
    template_name = 'roomdashboard_new.html'
    success_url = reverse_lazy('roomdashboard_list')
    login_url = 'login'

class BookedRoomDashboardListView(LoginRequiredMixin, SuperuserRequiredMixin, ListView):
    model = BookedRoom
    template_name = 'bookedroomdashboard_list.html'
    login_url = 'login'
