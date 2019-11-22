from django.urls import path

from .views import (
    RoomDashboardListView,
    RoomDashboardUpdateView,
    RoomDashboardDetailView,
    RoomDashboardDeleteView,
    RoomDashboardCreateView,
    BookedRoomDashboardListView,
)

urlpatterns = [
    path('rooms/<int:pk>/edit/',
         RoomDashboardUpdateView.as_view(), name='roomdashboard_edit'),
    path('rooms/<int:pk>/',
         RoomDashboardDetailView.as_view(), name='roomdashboard_detail'),
    path('rooms/<int:pk>/delete/',
         RoomDashboardDeleteView.as_view(), name='roomdashboard_delete'),
    path('rooms/new/',
         RoomDashboardCreateView.as_view(), name='roomdashboard_new'),
    path('rooms/', RoomDashboardListView.as_view(), name='roomdashboard_list'),
    path('bookedrooms/',
         BookedRoomDashboardListView.as_view(), name='bookedroomdashboard_list'),
]
