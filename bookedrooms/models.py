from django.conf import settings
from django.contrib.auth import get_user_model
from rooms.models import RoomCategory
from django.db import models
from django.urls import reverse

from computed_property import ComputedIntegerField

class BookedRoom(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    nbr_of_rooms = models.IntegerField(default=1)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    room_category = models.ForeignKey(
        RoomCategory,
        on_delete=models.CASCADE,
    )

    @property
    def total_cost(self):
        return (self.end_date - self.start_date).days * self.room_category.price * self.nbr_of_rooms

    def __str__(self):
        return self.room_category.category_name + " |  " + self.user.username
