from django import forms
from .models import ITInventory,Building,Department




class InputForm(forms.ModelForm):
    class Meta:
        model = ITInventory
        fields = ['asset_tag','asset_description','category','class_details','stwd_last_name','stwd_first_name',
                     'last_inventory_date','accqusation_date','cost','manufacturer','model_details','serial_number',
                     'department', 'building', 'room', 'vendor', 'notes']


class EditForm(forms.ModelForm):
    class Meta:
        model = ITInventory
        fields = ['asset_description','category','class_details','stwd_last_name','stwd_first_name',
                     'last_inventory_date','accqusation_date','cost','manufacturer','model_details','serial_number',
                     'department', 'building', 'room', 'vendor', 'notes']
                     
