from django.contrib import admin

# Register your models here.
from .models import Room,Building,Department,Manufacturer,ITInventory, Steward,Vendor,Models, Category
admin.site.register(Room)
admin.site.register(Building)
admin.site.register(Department)
admin.site.register(Manufacturer)
admin.site.register(ITInventory)
admin.site.register(Steward)
admin.site.register(Vendor)
admin.site.register(Models)
admin.site.register(Category)
