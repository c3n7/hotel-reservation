from django.db import models
from django.db.models import Sum
from django.urls import reverse


class RoomCategory(models.Model):
    category_name = models.CharField(max_length=20)
    summary = models.TextField()
    room_image = models.ImageField(
        upload_to='images/roomCategories',
        default='images/roomCategories/none.png'
    )
    price = models.IntegerField()
    total_rooms = models.IntegerField()

    @property
    def remaining_rooms(self):
        remaining = BookedRoom.objects.filter(
            room_category__category_name=self.category_name).aggregate(
                Sum('nbr_of_rooms'))['nbr_of_rooms__sum']
        if remaining is None:
            return self.total_rooms
        else:
            return self.total_rooms - remaining


    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('roomdashboard_detail', args=[str(self.id)])

from bookedrooms.models import BookedRoom
