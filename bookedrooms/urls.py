from django.urls import path

from .views import (
    BookedRoomsListView,
    BookedRoomsDetailView,
    BookedRoomsUpdateView,
    BookedRoomsDeleteView,
    BookedRoomsCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/',
         BookedRoomsUpdateView.as_view(),
         name='bookedrooms_edit'),
    path('<int:pk>/',
         BookedRoomsDetailView.as_view(),
         name='bookedrooms_detail'),
    path('<int:pk>/delete/',
         BookedRoomsDeleteView.as_view(),
         name='bookedrooms_delete'),
    path('new/<int:room_pk>/',
         BookedRoomsCreateView.as_view(),
         name='bookedrooms_new'),
    path('',
         BookedRoomsListView.as_view(),
         name='bookedrooms_list'),
]
