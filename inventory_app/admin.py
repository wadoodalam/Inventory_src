from django.contrib import admin

# Register your models here.
from .models import Building,Department,Manufacturer,ITInventory, Steward, Room,Vendor,Models, Category

admin.site.register(Building)
admin.site.register(Department)
admin.site.register(Manufacturer)
admin.site.register(ITInventory)
admin.site.register(Steward)
admin.site.register(Room)
admin.site.register(Vendor)
admin.site.register(Models)
admin.site.register(Category)
