from django.db import models

# Create your models here.
class Building(models.Model):
    building_name = models.CharField(max_length = 100)
    building_address = models.CharField(max_length = 500)
    def __str__(self):
        return self.building_name

class Department(models.Model):
    dept_name = models.CharField(max_length = 100)
    dept_type = models.CharField(max_length = 100)

    def __str__(self):
        return self.dept_name

class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.manufacturer_name

class ITInventory (models.Model):
    asset_tag = models.CharField(max_length=10, primary_key=True, blank = True)
    asset_description = models.CharField(max_length=50, blank = True)
    category = models.CharField(max_length=50)
    class_details = models.CharField(max_length=100)
    stwd_last_name = models.CharField(max_length=30)
    stwd_first_name= models.CharField(max_length=30)
    last_inventory_date = models.DateField()
    accqusation_date = models.DateField()
    cost = models.FloatField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete = models.CASCADE)
    model_details = models.CharField(max_length=500)
    serial_number = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
    building = models.ForeignKey(Building, on_delete = models.CASCADE, default='',blank = True)
    room = models.CharField(max_length = 100)
    vendor = models.CharField(max_length=100)
    notes = models.TextField()


    def __str__(self) :
        return self.asset_description
