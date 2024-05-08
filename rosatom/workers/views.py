from django.shortcuts import render


import json


def positions_page(request):
    return render(request, "workers/positions.html")


def create_position_page(request):
    return render(request, "workers/create_position.html")


def update_position_page(request, position_id):
    context = {"id": json.dumps(position_id)}
    return render(request, "workers/update_position.html", context)
