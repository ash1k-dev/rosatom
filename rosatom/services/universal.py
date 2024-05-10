def check_russian_letters(name):
    """
    Проверка, что все символы в строке являются буквами
    из определенного алфавита (по умолчанию - русский)
    """
    alphabet = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя ")
    return all(char.lower() in alphabet for char in name)


def check_and_refactor(name, data_source):
    """
    Проверка и приведение к единственной форме
    для ФИО и должности (в зависимости от источника данных)
    """
    if check_russian_letters(name):
        if data_source == "employee":
            return name.title()
        elif data_source == "position":
            return name.capitalize()
