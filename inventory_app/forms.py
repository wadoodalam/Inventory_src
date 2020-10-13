from django import forms
from .models import Room,Building,  Department, Manufacturer, Steward, Models, Vendor, ITInventory, Category



class InputForm(forms.ModelForm):
    class Meta:
        model = ITInventory
        fields = ['asset_tag','asset_description','category','class_details','stwd_name',
                     'last_inventory_date','accqusation_date','cost','manufacturerID','model_details','serial_number',
                     'departmentID', 'vendor','room', 'notes' ]


class EditForm(forms.ModelForm):
    class Meta:
        model = ITInventory
        fields = ['asset_description','category','class_details','stwd_name',
                     'last_inventory_date','accqusation_date','cost','manufacturerID','model_details','serial_number',
                     'departmentID', 'vendor', 'room','notes']

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['building_name', 'building_address']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_type']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name','dept_type','dept_building_name']

class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['manufacturer_name']

class ModelForm(forms.ModelForm):
    class Meta:
        model = Models
        fields = ['model_number', 'model_manufacturer_name']

class StewardForm(forms.ModelForm):
    class Meta:
        model = Steward
        fields = ['stwd_first_name', 'stwd_last_name' ,'stwd_email']

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['vendor_name', 'vendor_email', 'vendor_supplier']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_num', 'building']
