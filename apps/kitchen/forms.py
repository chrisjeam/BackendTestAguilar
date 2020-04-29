from django import forms
from apps.kitchen.models import Food, Menu, Combo
from datetime import datetime


class DateInput(forms.DateInput):
	input_type = 'date'

class FoodForm(forms.ModelForm):
	class Meta:
		model = Food
		fields = '__all__'
		labels = {
			'name': 'Nombre',
			'exceptions': 'Excepciones'
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'exceptions': forms.CheckboxSelectMultiple()
		}

class ComboForm(forms.ModelForm):
	class Meta:
		model = Combo
		fields = '__all__'
		labels = {
			'name': 'Nombre',
			'food': 'Comidas'
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'food': forms.CheckboxSelectMultiple()
		}


class MenuForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(MenuForm, self).__init__(*args, **kwargs)
		self.fields['date'].initial = datetime.now

	class Meta:
		model = Menu
		fields = '__all__'
		labels = {
			'name': 'Nombre',
    		'date': 'Fecha',
    		'combo': 'Combos',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'date': DateInput(attrs={'class':'form-control'}),
			'combo': forms.CheckboxSelectMultiple()  
		}