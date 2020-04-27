from django.urls import path
from apps.diner.views import *

urlpatterns = [
    path('/', Index, name='dinerIndex'),
]