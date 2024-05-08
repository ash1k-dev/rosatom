from django.contrib.admin import ModelAdmin, register

from .models import Employee, Position


@register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display = ("name", "sex", "position", "birth_date")
    list_filter = ("sex", "position", "position__category")


@register(Position)
class PositionAdmin(ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("name", "category")
