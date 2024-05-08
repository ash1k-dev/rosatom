# Тестовое задание на позицию backend разработчика в ФГУП Комбинат Электрохимприбор

Задание:
Требуется разработать базу данных и приложение для ведения списка сотрудников, с указанием их должностей. 
Приложение (сайт) должно поддерживать следующий функционал:
- Отображение списка должностей. Поля «должность», «категория» (выбор из вариантов: руководитель, специалист, служащий, рабочий);
- Добавление, удаление, изменение должностей через интерфейс приложения;
- Отображение списка сотрудников. Поля «ФИО», «пол», «возраст», «должность», «категория»;
- Добавление, удаление сотрудника;
- Просмотр и редактирование личной карточки сотрудника. Поля: «ФИО», «пол», «возраст». Выбор должности из списка.


Настройка:
1. Клонируйте репозиторий:
   - git clone https://github.com/ash1k-dev/rosatom

2. Установите нужные для работы библиотеки:
   - pip install -r requirements.txt

3. Настройте базу данных:
   - Установите PostgreSQL и создайте базу данных (для создания бд можете использовать файл (sql) со скриптами).
   - Добавьте данные для соединения в файл '.env'.

4. Запустите приложение:
   python manage.py runserver

   
Автор проекта: Роман Третьяков(https://github.com/ash1k-dev)
