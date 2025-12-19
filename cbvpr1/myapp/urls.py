from django.urls import path
from myapp.views import EmployeeCreateView,EmployeeListView,EmployeeDetailView,EmployeeUpdateView,EmployeeDeleteView

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee_list'),

    path('add/', EmployeeCreateView.as_view(), name='employee_create'),

    path('<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),

    path('<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee_update'),

    path('<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
]
