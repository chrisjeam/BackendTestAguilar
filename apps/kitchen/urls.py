from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.kitchen.views import *

urlpatterns = [
    path('', login_required(KitchenView.as_view()), name='kitchen_view'),
    path('foods', login_required(FoodListView.as_view()), name='food_list_view'),
    path('foods/new-food', login_required(FoodCreateView.as_view()), name='food_create_view'),
    path('foods/delete-food/<int:pk>', login_required(FoodDeleteView.as_view()), name='food_delete_view'),
    path('foods/new-combo', login_required(ComboCreateView.as_view()), name='combo_create_view'),
    path('foods/delete-combo/<int:pk>', login_required(ComboDeleteView.as_view()), name='combo_delete_view'),
    path('menus', login_required(MenuListView.as_view()), name='menu_list_view'),
    path('menus/new-menu', login_required(MenuCreateView.as_view()), name='menu_create_view'),
    path('menus/delete-menu/<int:pk>', login_required(MenuDeleteView.as_view()), name='menu_delete_view'),
]
