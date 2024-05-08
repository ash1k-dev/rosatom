from datetime import datetime


def calculate_age(birth_date):
    """Функция для вычисления возраста сотрудника"""
    date_now = datetime.now().date()
    age = int((date_now - birth_date).days / 365.25)
    return age
