from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('kitchen', include('apps.kitchen.urls')),
	path('diner', include('apps.diner.urls')),
]
