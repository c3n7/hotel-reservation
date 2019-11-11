from django.db import models
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

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('roomdashboard_detail', args=[str(self.id)])
