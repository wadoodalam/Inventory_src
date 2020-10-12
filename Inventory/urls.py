"""Inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventory_app import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.Home, name='home'),
    path('', views.Home, name='home'),

    path('insert/', views.Input_entry, name='Input'),
    path('category/', views.Category_entry, name='category'),
    path('department/', views.Department_entry, name='department'),
    path('manu/', views.Manufacturer_entry, name='manufacturer'),
    path('models/', views.Models_entry, name='models'),
    path('stwd/', views.Steward_entry, name='steward'),
    path('vendor/', views.Vendor_entry, name='vendor'),
    path('building/', views.Building_entry, name='building'),
    path('room/', views.Room_entry, name='room'),

    path('view/', views.list, name='view'),
    path('view/<int:asset_tag>/delete', views.delete, name='delete'),
    path('view/<int:asset_tag>', views.update, name='edit'),
    path('accounts/',include('registration.backends.default.urls'))
    #url(r'^accounts/', include('registration.backends.default.urls')),
]
