from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.diner.views import DinerView

urlpatterns = [
    path('', login_required(DinerView.as_view()), name='diner_view'),
]