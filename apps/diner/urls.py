from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.diner.views import *

urlpatterns = [
    path('', login_required(DinerView.as_view()), name='diner_view'),
    path('slack-bot', login_required(slackSubmit), name='slack_bot'),    
]