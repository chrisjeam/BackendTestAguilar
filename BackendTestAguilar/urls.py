from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from apps.user.views import LoginFormView, HomeView


urlpatterns = [
	path('', HomeView.as_view() , name='index'),
	path('login/', LoginFormView.as_view(), name= 'login'),
	path('logout/', login_required(LogoutView.as_view(next_page='login')), name='logout'),
	path('kitchen/', include('apps.kitchen.urls')),
	path('diner/', include('apps.diner.urls')),
	path('employee/', include('apps.user.urls')),
]
