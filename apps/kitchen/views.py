from django.shortcuts import render, redirect
from apps.kitchen.models import *
from datetime import datetime

# Create your views here.
def Index(request):
	data = {
		'fecha': datetime.now(),
		'orders': []
	}
	return render(request, 'kitchen.html', {'data': data})

