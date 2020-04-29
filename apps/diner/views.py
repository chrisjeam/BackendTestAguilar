from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
from django.http import HttpResponse
from datetime import datetime
from apps.kitchen.models import Menu, Order, Combo, Employee
from apps.diner.models import Employee
from apps.diner.forms import OrderForm
from slack import WebClient
from slack.errors import SlackApiError
import requests, json, os

# Create your views here.

class DinerView(View):
	
	def get(self, request):
		try:
			today = datetime.now()
			now = today.strftime('%d/%m/%Y')
			hour = today.hour
			query = Menu.objects.get(date=today)
			if query:
				menu = query
			else:
				menu = []
			return render(request, 'diner.html', {'menu': menu, 'timeNow': now, 'hour': hour})
		except Exception as e:
			print(e)
			return render(request, 'diner.html', {'timeNow': today})
	def post(self, request):
		today = datetime.now()
		data = request.POST
		combo_query = Combo.objects.get(pk=data['combo'])
		employee_query = Employee.objects.get(pk=1)
		order = Order(date=today, combo=combo_query, employee=employee_query)
		order.save()
		return redirect('diner_index')


class OrderCreateView(CreateView):
	model = Order
	template_name = 'create-order.html'
	form_class = OrderForm
	success_url = reverse_lazy('menu_list_view')


def slackSubmit(request):
	# Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
	webhook_url = 'https://hooks.slack.com/services/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'
	slack_data = {
	"blocks": [
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "Hey... ya está listo el menú de hoy... Yumi!"
				}
			},
			{
				"type": "divider"
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "*Windsor Court Hotel>*\n{{}}"
				}
			},
			{
				"type": "divider"
			}
		]
	}

	response = requests.post(
		webhook_url, data=json.dumps(slack_data),
		headers={'Content-Type': 'application/json'}
	)
	return HttpResponse(response)