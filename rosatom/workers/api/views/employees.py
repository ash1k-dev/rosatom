from django.db import connection
from django.shortcuts import redirect

from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from services.employee import calculate_age, check_and_refactor_name
from datetime import datetime


def check_exist_employee(birth_date, cursor, name):
    """
    Проверка существования сотрудника с такой же датой рождения и ФИО
    (существование сотрудника с таким же ФИО (полный тезка),
    но другой датой рождения допускается)
    """
    cursor.execute(
        "SELECT * FROM workers_employee WHERE name = %s AND birth_date = %s",
        [name, birth_date],
    )
    exist_user = cursor.fetchone()
    return exist_user


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
            " WHERE workers_employee.id = %s",
            [employee_id],
        )
        result = cursor.fetchone()
    position = {
        "id": result[0],
        "name": result[1],
        "sex": result[2],
        "birth_date": result[3],
        "position_id": result[4],
        "position_name": result[5],
        "position_category": result[6],
    }
    return JsonResponse(position, safe=False)


@csrf_exempt
def create_employee(request):
    """Создание нового сотрудника"""
    data = json.loads(request.body)
    name = check_and_refactor_name(data["name"])
    sex = data["sex"]
    position_id = data["position_id"]
    birth_date = datetime.fromisoformat(data["birth_date"])
    if name is None:
        return JsonResponse({"status": "wrong language"})
    if calculate_age(birth_date) < 18:
        return JsonResponse({"status": "too young"})
    if request.method == "POST":
        with connection.cursor() as cursor:
            exist_user = check_exist_employee(birth_date, cursor, name)
            if exist_user:
                return JsonResponse({"status": "already exists"})
            else:
                cursor.execute(
                    "INSERT INTO workers_employee (name,sex,birth_date,position_id) VALUES (%s, %s, %s, %s)",
                    [name, sex, birth_date, position_id],
                )
                return JsonResponse({"status": "success"})


@csrf_exempt
def delete_employee(request):
    """Удаление сотрудника"""
    data = json.loads(request.body)
    employee_id = int(data["id"])
    if request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM workers_employee WHERE id = %s", [employee_id])
    return JsonResponse({"status": "success"})


@csrf_exempt
def update_employee(request):
    """Редактирование сотрудника"""
    data = json.loads(request.body)
    employee_id = data["id"]
    name = check_and_refactor_name(data["name"])
    sex = data["sex"]
    birth_date = datetime.fromisoformat(data["birth_date"])
    position_id = data["position_id"]
    if name is None:
        return JsonResponse({"status": "wrong language"})
    if calculate_age(birth_date) < 18:
        return JsonResponse({"status": "too young"})
    if request.method == "POST":
        with connection.cursor() as cursor:
            exist_user = check_exist_employee(birth_date, cursor, name)
            if exist_user:
                return JsonResponse({"status": "already exists"})
            else:
                cursor.execute(
                    "UPDATE workers_employee SET name = %s, sex = %s, birth_date = %s, position_id = %s WHERE id = %s",
                    [name, sex, birth_date, position_id, employee_id],
                )
                return JsonResponse({"status": "success"})
