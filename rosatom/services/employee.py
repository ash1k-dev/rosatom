from datetime import datetime


def calculate_age(birth_date):
    """Вычисление возраста по дате рождения"""
    today = datetime.today()
    age = (
        today.year
        - birth_date.year
        - ((today.month, today.day) < (birth_date.month, birth_date.day))
    )
    return age
