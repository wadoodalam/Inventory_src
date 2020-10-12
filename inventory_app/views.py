from django.shortcuts import (get_object_or_404,  render,  HttpResponseRedirect,)
from .models import ITInventory,Building,Department,Category,Manufacturer, Models, Steward, Vendor
from django.db.models import Q
from django.views.generic import UpdateView
from .forms import RoomForm, BuildingForm, InputForm, EditForm, CategoryForm, DepartmentForm, ManufacturerForm, ModelForm, StewardForm, VendorForm
from django.shortcuts import render, redirect, get_object_or_404
import logging
from django.http import HttpResponse
import csv
import logging
from itertools import chain

# Create your views here.
def  Home (request):
    return render (request, "base.html")

def Input_entry(request):
    form = InputForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/view')
    context = {
    "form": form,
        }
    return render(request, "input.html",context)

def Category_entry(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/view')
    context = {
    "form": form,
        }
    return render(request, "category.html",context)

def Department_entry(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/view')
    context = {
    "form": form,
        }
    return render(request, "department.html",context)

def Manufacturer_entry(request):
    form = ManufacturerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/view')
    context = {
    "form": form,
        }
    return render(request, "manu.html",context)

def Models_entry(request):
    form = ModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/view')
    context = {
    "form": form,
        }
    return render(request, "models.html",context)

def Steward_entry(request):
    form = StewardForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/view')
    context = {
    "form": form,
        }
    return render(request, "stwd.html",context)

def Vendor_entry(request):
    form = VendorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/view')
    context = {
    "form": form,
        }
    return render(request, "vendor.html",context)

def Building_entry(request):
    form = BuildingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/view')
    context = {
    "form": form,
        }
    return render(request, "building.html",context)

def Room_entry(request):
    form = RoomForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/view')
    context = {
    "form": form,
        }
    return render(request, "room.html",context)


def Department_entry(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/view')
    context = {
    "form": form,
        }
    return render(request, "department.html",context)

def list(request):
    if request.GET.get('q') is not None:
        query = request.GET.get('q')
        IT_queryset = ITInventory.objects.filter(Q(asset_tag__iexact = query) | Q(asset_description__icontains = query) | Q(buildingID__building_name__iexact = query) |
        Q(accqusation_date__icontains = query) | Q(last_inventory_date__icontains = query) | Q(cost__iexact = query)| Q(model_details__model_number__iexact = query) |
        Q(serial_number__iexact = query) | Q(departmentID__dept_name__iexact = query) | Q(room__room_number__iexact = query) | Q(vendor__vendor_name__iexact = query) |
        Q(manufacturerID__manufacturer_name__iexact = query) | Q(notes__icontains = query) | Q(stwd_name__stwd_name__icontains = query))
        context={
                "IT_queryset": IT_queryset,

                }
        if request.GET.get('generate report') is not None:
            return generate_report(request, IT_queryset)
        return render(request,"view.html", context)

    IT_queryset = ITInventory.objects.all()


    context={
        "IT_queryset": IT_queryset,

    }

    if request.GET.get('generate report') is not None:
        return generate_report(request, IT_queryset)
    return render(request,"view.html", context)

def generate_report(request, IT_queryset):
    logger = logging.getLogger(__name__)
    logger.error(request)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename = "Inventory Report.csv" '
    writer = csv.writer(response)
    writer.writerow(['asset_tag','asset_description','category','class_details','stwd_name''last_inventory_date','accqusation_date','cost','manufacturer','model_details','serial_number','department', 'building', 'room', 'vendor', 'notes'])
    for row in IT_queryset:
        writer.writerow([row.asset_tag, row.asset_description, row.category, row.class_details, row.stwd_name,
                        row.last_inventory_date, row.accqusation_date, row.cost, row.manufacturerID, row.model_details, row.serial_number,
                        row.departmentID, row.buildingID, row.room, row.vendor, row.notes])
    return response

def delete(request,asset_tag = None):
    instance = get_object_or_404(ITInventory, asset_tag = asset_tag)
    instance.delete();
    return redirect('/view')

def update(request, asset_tag = None):
    instance = get_object_or_404(ITInventory, asset_tag = asset_tag)
    form = EditForm(request.POST or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit = False)
        instance = form.save()
        return redirect('/view')
    context = {
    "instance": instance,
    "form": form,
    }
    return render(request,"input.html", context)
