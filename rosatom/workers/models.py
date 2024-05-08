from django.db import models

ROLE = (
    ("Руководитель", "Руководитель"),
    ("Специалист", "Специалист"),
    ("Служащий", "Служащий"),
    ("Рабочий", "Рабочий"),
)

SEX = (
    ("Мужчина", "Мужчина"),
    ("Женщина", "Женщина"),
)

class Employee(models.Model):
    """Модель сотрудника"""

    name = models.CharField(max_length=100, verbose_name="ФИО")
    sex = models.CharField(choices=SEX, max_length=100, verbose_name="Пол")
    position = models.ForeignKey("Position", max_length=100, verbose_name="Должность")
    birth_date = models.DateField(verbose_name="Дата рождения")

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        unique_together = (("name", "birth_date",),)
        ordering = ["name"]

    def __str__(self):
        return self.name


class Position(models.Model):
    """Модель должности"""

    name = models.CharField(max_length=100, verbose_name="Должность", unique=True)
    category = models.CharField(choices=ROLE, max_length=100, verbose_name="Категория")

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.name
