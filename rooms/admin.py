from django.contrib import admin

from .models import RoomCategory

class RoomCategoryAdmin(admin.ModelAdmin):
    model = RoomCategory
    list_display = ['category_name', 'summary', 'price', 'total_rooms', 'remaining_rooms']
    readonly_fields = ('remaining_rooms',)

admin.site.register(RoomCategory, RoomCategoryAdmin)
