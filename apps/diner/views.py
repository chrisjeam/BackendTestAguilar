from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
from django.contrib.auth.models import User
from datetime import datetime
from apps.kitchen.models import Menu, Order, Combo
from slack import WebClient
from slack.errors import SlackApiError

# Create your views here.

class DinerView(View):	
	def get(self, request):
		today = datetime.now()
		now = today.strftime('%d/%m/%Y')
		hour = today.hour
		try:
			menu_query = Order.objects.get(date=today)
		except Order.DoesNotExist:
			menu_query = None
		try:
			query = Menu.objects.get(date=today)			
		except Menu.DoesNotExist:
			query = None
		return render(request, 'diner.html', {'menu': query, 'timeNow': now, 'hour': hour, 'last_menu': menu_query})
	def post(self, request):
		today = datetime.now()
		data = request.POST
		combo_query = Combo.objects.get(pk=data['menu'])
		employee_query = User.objects.get(pk=request.user.id)
		order = Order(date=today, combo=combo_query, employee=employee_query)
		slackSubmit(order.id)
		order.save()
		return redirect('diner_view')

