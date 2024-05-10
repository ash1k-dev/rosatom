from datetime import datetime


def refactor_name(name):
    """Приведение к единственной форме для ФИО"""
    name = name.title()
    return name


def check_russian_letters(name):
    """Проверка, что все символы в строке являются буквами русского алфавита"""
    russian_alphabet = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя ")
    return all(char.lower() in russian_alphabet for char in name)


def check_and_refactor_name(name):
    """Проверка и приведение к единственной форме для ФИО"""
    if check_russian_letters(name):
        name = name.title()
        return name


def calculate_age(birth_date):
    """Вычисление возраста по дате рождения"""
    today = datetime.today()
    age = (
        today.year
        - birth_date.year
        - ((today.month, today.day) < (birth_date.month, birth_date.day))
    )
    return age
