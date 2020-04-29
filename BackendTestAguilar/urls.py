from django.urls import path, include
from apps.user.views import LoginFormView, RegisterFormView

urlpatterns = [
	path('login/', LoginFormView.as_view(), name= 'login'),
	path('register/', RegisterFormView.as_view(), name='register'),
	path('kitchen/', include('apps.kitchen.urls')),
	path('diner/', include('apps.diner.urls')),
]
