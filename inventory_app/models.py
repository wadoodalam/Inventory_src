from django.db import models

# Create your models here.
class Room(models.Model):
    room_number = models.CharField(max_length = 200)
    def __str__(self):
        return self.room_number

class Building(models.Model):
    building_name = models.CharField(max_length = 100)
    building_address = models.CharField(max_length = 500)

    def __str__(self):
        return self.building_name

class Department(models.Model):
    dept_name = models.CharField(max_length = 100)
    dept_type = models.CharField(max_length = 100)
    dept_building_name = models.ForeignKey(Building, on_delete = models.CASCADE)

    def __str__(self):
        return self.dept_name

class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.manufacturer_name

class Steward(models.Model):
    stwd_name = models.CharField(max_length = 500)
    stwd_email = models.CharField(max_length = 500)
    stwd_buidling_name = models.ForeignKey(Building, on_delete = models.CASCADE)
    stwd_room = models.ForeignKey(Room, on_delete = models.CASCADE)
    def __str__(self):
        return self.stwd_name

class Models(models.Model):
    model_number = models.CharField(max_length = 500)
    model_manufacturer_name = models.ForeignKey(Manufacturer, on_delete = models.CASCADE)
    def __str__(self):
        return self.model_number

class Vendor(models.Model):
    vendor_name =  models.CharField(max_length = 500)
    vendor_email = models.CharField(max_length = 500,default='')
    vendor_supplier = models.ForeignKey(Manufacturer, on_delete = models.CASCADE)
    def __str__(self):
        return self.vendor_name

class Category(models.Model):
    category_type = models.CharField(max_length = 500)
    def __str__(self):
        return self.category_type


class ITInventory (models.Model):
    asset_tag = models.CharField(max_length=10, primary_key=True)
    asset_description = models.CharField(max_length=50, blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    class_details = models.CharField(max_length=100)
    stwd_name = models.ForeignKey(Steward, on_delete = models.CASCADE)
    last_inventory_date = models.DateField()
    accqusation_date = models.DateField()
    cost = models.FloatField()
    manufacturerID = models.ForeignKey(Manufacturer, on_delete = models.CASCADE)
    model_details = models.ForeignKey(Models, on_delete = models.CASCADE)
    serial_number = models.CharField(max_length=100)
    departmentID = models.ForeignKey(Department, on_delete = models.CASCADE)
    buildingID = models.ForeignKey(Building, on_delete = models.CASCADE, default='')
    room =  models.ForeignKey(Room, on_delete = models.CASCADE, default='')
    vendor = models.ForeignKey(Vendor, on_delete = models.CASCADE)
    notes = models.TextField()


    def __str__(self) :
        return self.asset_tag
