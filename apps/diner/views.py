from django.shortcuts import render
from datetime import datetime

# Create your views here.
def Index(request):
	data = {
		'fecha': datetime.now(),
		'combos': []
	}
	return render(request, 'diner.html', {'data': data})