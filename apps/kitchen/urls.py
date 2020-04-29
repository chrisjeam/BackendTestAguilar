from django.urls import path
from apps.kitchen.views import *

urlpatterns = [
    path('', KitchenView.as_view(), name='kitchen_view'),
    path('foods', FoodListView.as_view(), name='food_list_view'),
    path('foods/new-food', FoodCreateView.as_view(), name='food_create_view'),
    path('foods/delete-food/<int:pk>', FoodDeleteView.as_view(), name='food_delete_view'),
    path('foods/new-combo', ComboCreateView.as_view(), name='combo_create_view'),
    path('foods/delete-combo/<int:pk>', ComboDeleteView.as_view(), name='combo_delete_view'),
    path('menus', MenuListView.as_view(), name='menu_list_view'),
    path('menus/new-menu', MenuCreateView.as_view(), name='menu_create_view'),
    path('menus/delete-menu/<int:pk>', MenuDeleteView.as_view(), name='menu_delete_view'),
]
