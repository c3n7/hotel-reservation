from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from rooms.models import RoomCategory
from bookedrooms.models import BookedRoom

class RoomDashboardListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = RoomCategory
    template_name = 'roomdashboard_list.html'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser

class RoomDashboardDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = RoomCategory
    template_name = 'roomdashboard_detail.html'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser

class RoomDashboardUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = RoomCategory
    fields = ('category_name', 'summary', 'room_image', 'price', 'total_rooms')
    template_name = 'roomdashboard_edit.html'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser

class RoomDashboardDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = RoomCategory
    template_name = 'roomdashboard_delete.html'
    success_url = reverse_lazy('roomdashboard_list')
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser

class RoomDashboardCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = RoomCategory
    fields = ('category_name', 'summary', 'room_image', 'price', 'total_rooms')
    template_name = 'roomdashboard_new.html'
    success_url = reverse_lazy('roomdashboard_list')
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser

class BookedRoomDashboardListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = BookedRoom
    template_name = 'bookedroomdashboard_list.html'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser
