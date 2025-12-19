from django.views.generic import ListView,DetailView,CreateView,UpdateView, DeleteView

from django.urls import reverse_lazy
from .models import Employee

# 1️⃣ LIST VIEW – Display all employees
class EmployeeListView(ListView):
    model = Employee
   
# 2️⃣ DETAIL VIEW – Display single employee details

class EmployeeDetailView(DetailView):
    model = Employee
 

# 3️⃣ CREATE VIEW – Add new employee
class EmployeeCreateView(CreateView):
    model = Employee
   
  

# 4️⃣ UPDATE VIEW – Edit employee
class EmployeeUpdateView(UpdateView):
    model = Employee
  

# 5️⃣ DELETE VIEW – Delete employee
class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee_list')
