from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.user.views import EmployeeListView, EmployeeFormView, EmployeeDeleteView



urlpatterns = [
    path('', login_required(EmployeeListView.as_view()), name='employee_list_view'),
	path('new-employee', login_required(EmployeeFormView.as_view()), name='employee_new_view'),
	path('delete-employee/<int:pk>', login_required(EmployeeDeleteView.as_view()), name='employee_delete_view'),
]