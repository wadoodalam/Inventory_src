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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('insert.html/', views.Input_entry, name='Input'),
    path('view.html/', views.list, name='view'),
    path('view.html/<asset_tag>/delete', views.delete, name='delete'),
    path('view.html/<asset_tag>/', views.update, name='edit'),
    # Ha, Can you please add the edit and delete button in the 'view.html' file. you see the url patterns up here^. Thanks
]
