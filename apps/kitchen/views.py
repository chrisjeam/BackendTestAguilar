from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.models import User
from datetime import datetime
from apps.kitchen.models import Order, Menu, Food, Combo
from apps.kitchen.forms import MenuForm, FoodForm, ComboForm
from apps.kitchen.tasks import sendSlackMessage

class KitchenView(ListView):
	model = Order
	template_name = 'kitchen.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['timeNow'] = datetime.now 
		return context


class FoodListView(ListView):
	model = Food
	template_name = 'foods/foods.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['combos'] = Combo.objects.all()
		return context

class FoodCreateView(CreateView):
	model = Food
	form_class = FoodForm
	template_name = 'foods/food_create_form.html'
	success_url = reverse_lazy('food_list_view')	 

class FoodDeleteView(DeleteView):
	model = Food
	form_class = FoodForm
	template_name = 'foods/food_delete.html'
	success_url = reverse_lazy('food_list_view')

class ComboCreateView(CreateView):
	model = Combo
	form_class = ComboForm
	template_name = 'foods/combo_create_form.html'
	success_url = reverse_lazy('food_list_view')	 

class ComboDeleteView(DeleteView):
	model = Combo
	form_class = ComboForm
	template_name = 'foods/combo_delete.html'
	success_url = reverse_lazy('food_list_view')

class MenuListView(ListView):
	model = Menu
	template_name = 'menus/menus.html'

class MenuCreateView(CreateView):
	model = Menu
	form_class = MenuForm
	template_name = 'menus/menu_create_form.html'
	success_url = reverse_lazy('menu_list_view')
	
	def form_valid(self, form):
		self.object = form.save()
		sendSlackMessage(self.object.id)
		return super().form_valid(form)

class MenuDeleteView(DeleteView):
	model = Menu
	form_class = MenuForm
	template_name = 'menus/menu_delete.html'
	success_url = reverse_lazy('menu_list_view')

	
