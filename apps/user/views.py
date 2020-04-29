from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from apps.user.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect

# Create your views here.
class RegisterFormView(CreateView):
	model = User
	template_name = 'register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('login')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['message'] = ''
		return context

# def RegisterFormView(request):
# 	form_class = UserCreationForm()
# 	if request.method == 'POST':
# 		form_class = UserCreationForm(request.POST)
# 		if form_class.is_valid():
# 			form_class.save()

# 	context={'form':form_class}
# 	return render(request, 'register.html', context)

class LoginFormView(LoginView):
	template_name = 'login.html'

	def dispatch(self, request, *args, **kwargs):
		print(request.user)
		return super().dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['message'] = ''
		return context

# class LoginFormView(LoginView):
# 	form_class = AuthenticationForm
# 	template_name = 'login.html'
# 	success_url = reverse_lazy('kitchen_view')

# 	def dispatch(self, request, *args, **kwargs):
# 		print(request.user)
# 		return super().dispatch(request, *args, **kwargs)

# 	def form_valid(self, form):
# 		login(self.request, form.get_user())
# 		return HttpResponseRedirect(self.success_url)
