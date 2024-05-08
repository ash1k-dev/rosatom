from django.shortcuts import render


import json


def positions_page(request):
    """Представление для списка должностей"""
    return render(request, "workers/positions.html")


def create_position_page(request):
    """Представление для создания новой должности"""
    return render(request, "workers/create_position.html")


def update_position_page(request, position_id):
    """Представление для редактирования должности"""
    context = {"id": json.dumps(position_id)}
    return render(request, "workers/update_position.html", context)


def employees_page(request):
    """Представление для списка сотрудников"""
    return render(request, "workers/employees.html")


def create_employee_page(request):
    """Представление для создания нового сотрудника"""
    return render(request, "workers/create_employee.html")


def update_employee_page(request, employee_id):
    """Представление для редактирования сотрудника"""
    context = {"id": json.dumps(employee_id)}
    print(context)
    return render(request, "workers/update_employee.html", context)
