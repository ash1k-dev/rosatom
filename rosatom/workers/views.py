from django.db import connection
from django.shortcuts import render


import json

from workers.api.views.positions import get_positions


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
    result = get_positions_list()
    context = {"positions": result}
    return render(request, "workers/create_employee.html", context)


def update_employee_page(request, employee_id):
    """Представление для редактирования сотрудника"""
    result = get_positions_list()
    context = {"id": json.dumps(employee_id), "positions": result}
    return render(request, "workers/update_employee.html", context)


def get_positions_list():
    """Получение списка должностей из базы данных"""
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT workers_position.id,workers_position.name, workers_position.category"
            " FROM workers_position"
        )
        result = cursor.fetchall()
    return result
