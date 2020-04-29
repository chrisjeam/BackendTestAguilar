from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View, ListView, CreateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from apps.user.forms import RegisterForm

# Create your views here.
class EmployeeFormView(CreateView):
	model = User
	template_name = 'employees/employee_create_form.html'
	form_class = RegisterForm
	success_url = reverse_lazy('employee_list_view')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['message'] = ''
		return context

class EmployeeListView(ListView):
	model = User
	template_name = 'employees/employee.html'

class EmployeeDeleteView(DeleteView):
	model = User
	form_class = RegisterForm
	template_name = 'employees/employee_delete.html'
	success_url = reverse_lazy('employee_list_view')

class LoginFormView(LoginView):
	template_name = 'login.html'

	def dispatch(self, request, *args, **kwargs):
		print(request.user)
		return super().dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['message'] = ''
		return context
		
class LogoutFormView(LogoutView):
	next_page = reverse_lazy('login')
	#template_name = 'login.html'

	def dispatch(self, request, *args, **kwargs):
		print(request.users)
		return super().dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['message'] = ''
		return context

class HomeView(View):
	def get(self, request):	
		url_redirect = 'login'
		try:
			if request.user.username == 'nora':
				url_redirect = 'kitchen_view'
			else:	
				url_redirect = 'diner_view'
		except Exception as e:
			print(e)
	
		return redirect(url_redirect)
