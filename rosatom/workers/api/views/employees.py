from django.db import connection
from django.shortcuts import redirect

from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from services.calculate_age import calculate_age


def get_employees(request):
    """Получение списка сотрудников и их данных"""
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT workers_employee.id,workers_employee.name, workers_employee.sex, workers_employee.birth_date,"
            " workers_position.name, workers_position.category"
            " FROM workers_employee"
            " LEFT JOIN workers_position"
            " ON workers_employee.position_id = workers_position.id"
        )
        result = cursor.fetchall()
    employees = []
    for employee in result:
        employees.append(
            {
                "id": employee[0],
                "name": employee[1],
                "sex": employee[2],
                "age": calculate_age(employee[3]),
                "position_name": employee[4],
                "position_category": employee[5],
            }
        )
    return JsonResponse(employees, safe=False)


def get_employee(request, employee_id):
    """Получение данных о конкретном сотруднике"""
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT workers_employee.id,workers_employee.name, workers_employee.sex, workers_employee.birth_date,"
            "workers_position.id, workers_position.name, workers_position.category"
            " FROM workers_position"
            " LEFT JOIN workers_employee"
            " ON workers_employee.position_id = workers_position.id"
            " WHERE workers_position.id = %s",
            [employee_id],
        )
        result = cursor.fetchone()
    print(result)
    position = {
        "id": result[0],
        "name": result[1],
        "sex": result[2],
        "birth_date": result[3],
        "position_id": result[4],
        "position_name": result[5],
        "position_category": result[6],
    }
    print(position)
    return JsonResponse(position, safe=False)


@csrf_exempt
def create_employee(request):
    """Создание нового сотрудника"""
    data = json.loads(request.body)
    name = data["name"]
    sex = data["sex"]
    birth_date = data["birth_date"]
    position_id = data["position_id"]
    if calculate_age(birth_date) < 18:
        return JsonResponse({"success": False})
    if request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO workers_employee (name,sex,birth_date,position_id) VALUES (%s, %s, %s, %s)",
                [name, sex, birth_date, position_id],
            )
        return JsonResponse({"success": True})


def delete_employee(request, employee_id):
    """Удаление сотрудника"""
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM workers_employee WHERE id = %s", [employee_id])

    return redirect("workers:employees")


def update_employee(request, employee_id):
    """Редактирование сотрудника"""
    pass
