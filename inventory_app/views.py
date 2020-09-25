from django.shortcuts import (get_object_or_404,  render,  HttpResponseRedirect)
from .models import ITInventory,Building,Department
from django.views.generic import UpdateView
from .forms import InputForm

# Create your views here.
def  Home (request):
    return render (request, "home.html")

def Input_entry(request):
    form = InputForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
    "form": form,
        }
    return render(request, "input.html",context)


def list(request):
    queryset = ITInventory.objects.all()
    context = {
        "queryset": queryset,
    }
    return render (request, "view.html", context)



#class EditView(UpdateView):
    #model = ITInventory
    #fields : [
    #"asset_tag","asset_description"
    #]
    #success_url = "/"
