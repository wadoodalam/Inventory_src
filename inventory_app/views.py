from django.shortcuts import (get_object_or_404,  render,  HttpResponseRedirect)
from .models import ITInventory,Building,Department
from django.db.models import Q
from django.views.generic import UpdateView
from .forms import InputForm, EditForm
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def  Home (request):
    return render (request, "home.html")

def Input_entry(request):
    form = InputForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/view.html')
    context = {
    "form": form,
        }
    return render(request, "input.html",context)


def list(request):
    queryset = ITInventory.objects.all()
    context={
        "queryset": queryset,

        }
    return render(request,"view.html",context)

def search(request):
    if request.GET.get('q') is not None:
        query = request.GET.get('q')
        queryset = ITInventory.objects.filter(Q(asset_tag__iexact = query) | Q(asset_description__icontains = query) | Q(building__building_name__iexact = query) | Q(accqusation_date__icontains = query) | Q(last_inventory_date__icontains = query) | Q(cost__icontains = query)| Q(model_details__iexact = query) | Q(serial_number__icontains = query) | Q(department__dept_name__iexact = query) | Q(room__iexact = query) | Q(vendor__iexact = query) | Q(manufacturer__manufacturer_name__iexact = query))
        context={
                "queryset": queryset,
                }
        return render(request,"search.html", context)

    return render(request,"search.html")


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
