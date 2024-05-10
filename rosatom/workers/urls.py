from django.conf.urls import url

app_name = "workers"

from workers.api.views.employees import (create_employee, delete_employee,
                                         get_employee, get_employees,
                                         update_employee)
from workers.api.views.positions import (create_position, delete_position,
                                         get_position, get_positions,
                                         update_position)
from workers.views import (create_employee_page, create_position_page,
                           employees_page, positions_page,
                           update_employee_page, update_position_page)

urlpatterns = [
    # api для должностей
    url(r"^api/get-positions/$", get_positions),
    url(r"^api/get-position/(?P<position_id>\d+)/$", get_position),
    url(r"^api/create-position/$", create_position),
    url(r"^api/update-position/$", update_position),
    url(r"^api/delete-position/$", delete_position),
    # api для сотрудников
    url(r"^api/get-employees/$", get_employees),
    url(r"^api/get-employee/(?P<employee_id>\d+)/$", get_employee),
    url(r"^api/create-employee/$", create_employee),
    url(r"^api/update-employee/$", update_employee),
    url(r"^api/delete-employee/$", delete_employee),
    # Представления для должностей
    url(r"^positions/(?P<position_id>\d+)/$", update_position_page),
    url(r"^positions/$", positions_page, name="positions"),
    url(r"^positions/create/$", create_position_page, name="create_position"),
    # Представления для сотрудников
    url(r"^$", employees_page, name="employees"),
    url(r"^employees/create/$", create_employee_page, name="create_employee"),
    url(r"^employees/(?P<employee_id>\d+)/$", update_employee_page),
]
