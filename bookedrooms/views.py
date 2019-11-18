from braces.views import LoginRequiredMixin

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from bootstrap_datepicker_plus import DatePickerInput

from rooms.models import RoomCategory
from .models import BookedRoom

class BookedRoomsListView(LoginRequiredMixin, ListView):
    model = BookedRoom
    template_name = 'bookedroom_list.html'
    login_url = 'login'

    # Return only the data for the currently logged in user
    def get_queryset(self):
        return BookedRoom.objects.filter(
            user=self.request.user).order_by('start_date')

class BookedRoomsDetailView(LoginRequiredMixin, DetailView):
    model = BookedRoom
    template_name = 'bookedroom_detail.html'
    login_url = 'login'

class BookedRoomsUpdateView(LoginRequiredMixin, UpdateView):
    model = BookedRoom
    fields = ('room_category', 'nbr_of_rooms', 'start_date', 'end_date')
    template_name = 'bookedroom_edit.html'
    login_url = 'login'

    def get_form(self):
        form = super(BookedRoomsUpdateView, self).get_form()
        form.fields['start_date'].widget = DatePickerInput().start_of('duration')
        form.fields['end_date'].widget = DatePickerInput().end_of('duration')
        return form

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(BookedRoomsUpdateView, self).form_valid(form)

class BookedRoomsDeleteView(LoginRequiredMixin, DeleteView):
    model = BookedRoom
    template_name = 'bookedroom_delete.html'
    success_url = reverse_lazy('bookedrooms_list')
    login_url = 'login'

class BookedRoomsCreateView(LoginRequiredMixin, CreateView):
    model = BookedRoom
    fields = ('room_category', 'nbr_of_rooms', 'start_date', 'end_date')
    template_name = 'bookedroom_add.html'
    success_url = reverse_lazy('bookedrooms_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        """
        Overridden to ensure that the primary key passed
        does exist
        """
        self.room_category = get_object_or_404(RoomCategory, pk=kwargs['room_pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super(BookedRoomsCreateView, self).get_initial()
        initial['room_category'] = self.room_category
        return initial

    def get_form(self):
        """
        Overridden to change the DateFields from text boxes to
        DatePicker widgets
        """
        form = super(BookedRoomsCreateView, self).get_form()
        form.fields['start_date'].widget = DatePickerInput().start_of('duration')
        form.fields['end_date'].widget = DatePickerInput().end_of('duration')
        return form

    def form_valid(self, form):
        """
        Overridden to always set the user to the currently logged in user
        """
        user = self.request.user
        form.instance.user = user
        return super(BookedRoomsCreateView, self).form_valid(form)
