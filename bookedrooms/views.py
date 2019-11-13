from braces.views import LoginRequiredMixin

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import BookedRoom

class BookedRoomDetailView(LoginRequiredMixin, DetailView):
    model = BookedRoom
    template_name = 'bookedroom_detail.html'
    login_url = 'login'

class BookedRoomUpdateView(LoginRequiredMixin, UpdateView):
    model = BookedRoom
    fields = ('category_name', 'summary', 'room_image', 'price', 'total_rooms')
    template_name = 'bookedroom_edit.html'
    login_url = 'login'

class BookedRoomDeleteView(LoginRequiredMixin, DeleteView):
    model = BookedRoom
    template_name = 'bookedroom_cancel.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

class RoomDashboardCreateView(LoginRequiredMixin, CreateView):
    model = BookedRoom
    fields = ('category_name', 'summary', 'room_image', 'price', 'total_rooms')
    template_name = 'bookedroom_add.html'
    success_url = reverse_lazy('roomdashboard_list')
    login_url = 'login'

