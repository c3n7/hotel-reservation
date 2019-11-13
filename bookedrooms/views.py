from braces.views import LoginRequiredMixin

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import BookedRoom

class BookedRoomsListView(LoginRequiredMixin, ListView):
    model = BookedRoom
    template_name = 'bookedroom_list.html'
    login_url = 'login'

    # Return only the data for the currently logged in user
    def get_queryset(self):
        return BookedRoom.objects.filter(user=self.request.user).order_by('start_date')

class BookedRoomsDetailView(LoginRequiredMixin, DetailView):
    model = BookedRoom
    template_name = 'bookedroom_detail.html'
    login_url = 'login'

class BookedRoomsUpdateView(LoginRequiredMixin, UpdateView):
    model = BookedRoom
    fields = ('category_name', 'summary', 'room_image', 'price', 'total_rooms')
    template_name = 'bookedroom_edit.html'
    login_url = 'login'

class BookedRoomsDeleteView(LoginRequiredMixin, DeleteView):
    model = BookedRoom
    template_name = 'bookedroom_cancel.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

class BookedRoomsCreateView(LoginRequiredMixin, CreateView):
    model = BookedRoom
    fields = ('category_name', 'summary', 'room_image', 'price', 'total_rooms')
    template_name = 'bookedroom_add.html'
    success_url = reverse_lazy('roomdashboard_list')
    login_url = 'login'

