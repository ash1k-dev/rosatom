from django.db import connection

from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from services.position import refactor_position


def get_positions(request):
    """Получение списка должностей"""
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT workers_position.id,workers_position.name, workers_position.category"
            " FROM workers_position"
        )
        result = cursor.fetchall()
    positions = []
    for position in result:
        positions.append(
            {
                "id": position[0],
                "name": position[1],
                "category": position[2],
            }
        )
    return JsonResponse(positions, safe=False)


@csrf_exempt
def create_position(request):
    """Создание новой должности"""
    data = json.loads(request.body)
    name = refactor_position(data["name"])
    category = data["category"]
    if request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO workers_position (name,category) VALUES (%s, %s)",
                [name, category],
            )
        return JsonResponse({"status": "success"})


@csrf_exempt
def delete_position(request):
    """Удаление должности"""
    data = json.loads(request.body)
    position_id = data["id"]
    if request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM workers_position WHERE id = %s", [position_id])
    return JsonResponse({"status": "success"})


@csrf_exempt
def update_position(request):
    """Редактирование должности"""
    data = json.loads(request.body)
    position_id = int(data["id"])
    category = data["category"]
    name = refactor_position(data["name"])
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE workers_position SET name = %s, category = %s WHERE id = %s",
            [name, category, position_id],
        )
    return JsonResponse({"status": "success"})


def get_position(request, position_id):
    """Получение данных о конкретной должности"""
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT workers_position.id,workers_position.name, workers_position.category"
            " FROM workers_position"
            " WHERE workers_position.id = %s",
            [position_id],
        )
        result = cursor.fetchone()
    position = {
        "id": result[0],
        "name": result[1],
        "category": result[2],
    }
    return JsonResponse(position, safe=False)
