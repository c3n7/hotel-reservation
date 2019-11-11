from django.urls import path

from .views import (
    RoomDashboardListView,
    RoomDashboardUpdateView,
    RoomDashboardDetailView,
    RoomDashboardDeleteView,
    RoomDashboardCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/',
         RoomDashboardUpdateView.as_view(), name='roomdashboard_edit'),
    path('<int:pk>/',
         RoomDashboardDetailView.as_view(), name='roomdashboard_detail'),
    path('<int:pk>/delete/',
         RoomDashboardDeleteView.as_view(), name='roomdashboard_delete'),
    path('new/',
         RoomDashboardCreateView.as_view(), name='roomdashboard_new'),
    path('', RoomDashboardListView.as_view(), name='roomdashboard_list'),
]
