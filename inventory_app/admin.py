from django.contrib import admin

# Register your models here.
from .models import Building,Department,Manufacturer,ITInventory

admin.site.register(Building)
admin.site.register(Department)
admin.site.register(Manufacturer)
admin.site.register(ITInventory)
