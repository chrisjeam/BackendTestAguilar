from django import forms
from apps.kitchen.models import Food, Menu, Combo
from datetime import datetime

class OrderForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(MenuForm, self).__init__(*args, **kwargs)
		self.fields['date'].initial = datetime.now

	class Meta:
		model = Menu
		fields = '__all__'
		labels = {
			'combos': 'Combo'
		}
		widgets = {
			'combo': forms.CheckboxSelectMultiple()  
		}