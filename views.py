from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


def add_employee(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        department = request.POST['department']
        salary = request.POST['salary']
        join_date = request.POST['join_date']

        Employee.objects.create(
            name=name,
            email=email,
            department=department,
            salary=salary,
            join_date=join_date
        )

        return redirect('employee_list')

    return render(request, 'add_employee.html')


def edit_employee(request, id):
    employee = Employee.objects.get(id=id)

    if request.method == "POST":
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.department = request.POST['department']
        employee.salary = request.POST['salary']
        employee.join_date = request.POST['join_date']

        employee.save()
        return redirect('employee_list')

    return render(request, 'edit_employee.html', {'employee': employee})


def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('employee_list')