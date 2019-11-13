from django.contrib import admin

from .models import RoomCategory

class RoomCategoryAdmin(admin.ModelAdmin):
    model = RoomCategory
    list_display = ['category_name', 'summary', 'price', 'total_rooms']

admin.site.register(RoomCategory, RoomCategoryAdmin)
