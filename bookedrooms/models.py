from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from rooms.models import RoomCategory
from django.db import models
from django.urls import reverse
from django.db.models import Sum

from datetime import date, timedelta

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
        if self.start_date is not None and self.end_date is not None:
            return (self.end_date - self.start_date).days * self.room_category.price * self.nbr_of_rooms
        else:
            return 0

    def clean(self):

        # Loop through the start and end dates
        day = timedelta(days=1)
        start = self.start_date
        end = self.end_date
        current = start
        while current < end:
            print(current)
            # Retrieve booked rooms that fall into this date
            rooms = BookedRoom.objects.filter(
                start_date__lte=current,
                end_date__gt=current,
                room_category__category_name=self.room_category.category_name)
            print("\tNbr of results: {}".format(rooms.count()))

            # Sum the totals
            total_booked_rooms = 0
            for room in rooms:
                total_booked_rooms = total_booked_rooms + room.nbr_of_rooms

            total_available_rooms = RoomCategory.objects.filter(
                category_name=self.room_category.category_name)[0].total_rooms
            # Check if there is an instance of this room so as to
            # not add the current nbr_of_rooms
            current_room = BookedRoom.objects.filter(id=self.id)
            if current_room.count() == 1:
                remaining = total_available_rooms - total_booked_rooms + current_room[0].nbr_of_rooms
            else:
                remaining = total_available_rooms - total_booked_rooms

            print("\t\tRemaining Rooms: {}".format(remaining))
            print("\t\tNbr of rooms:{}".format(self.nbr_of_rooms))

            if self.nbr_of_rooms > remaining:
                raise ValidationError(
                    "On {} there are less rooms than you desire. ({} > {})".format(
                        current, self.nbr_of_rooms, remaining))
            current += day

    def __str__(self):
        return self.room_category.category_name + " |  " + self.user.username
