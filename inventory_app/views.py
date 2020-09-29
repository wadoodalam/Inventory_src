from django.shortcuts import (get_object_or_404,  render,  HttpResponseRedirect)
from .models import ITInventory,Building,Department
from django.views.generic import UpdateView
from .forms import InputForm, InventorySearchForm
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



def delete(request,asset_tag = None):
    instance = get_object_or_404(ITInventory, asset_tag = asset_tag)
    instance.delete();
    return redirect('/view.html')

def update(request, asset_tag = None):
    instance = get_object_or_404(ITInventory, asset_tag = asset_tag)
    form = InputForm(request.POST or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit = False)
        instance = form.save()
        return redirect('/view.html')
    context = {
    "instance": instance,
    "form": form,
    }
    return render(request,"input.html", context)



def list(request):
    queryset = ITInventory.objects.all()
    form = InventorySearchForm(request.POST or None)
    context={
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        queryset = ITInventory.objects.all().order_by('accqusation_date').filter(asset_tag__icontains=form['asset_tag'].value(), asset_description__icontains=form['asset_description'].value(),building__building_name__contains=form['building'].value())
        context={
        "queryset": queryset,
        "form": form,
        }
    return render(request,"view.html", context)
