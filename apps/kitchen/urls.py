from django.urls import path
from apps.kitchen.views import *

urlpatterns = [
    path('/', Index, name='index'),
]
