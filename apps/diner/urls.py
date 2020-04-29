from django.urls import path
from apps.diner.views import *

urlpatterns = [
    path('', DinerView.as_view(), name='diner_index'),
    path('create-order/<int:id>', OrderCreateView.as_view(), name='create_order'),
    path('slack-bot', slackSubmit, name='slack_bot'),

    
]