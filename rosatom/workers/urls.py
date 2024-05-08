from django.conf.urls import url

app_name = "workers"

from workers.views import (
    positions_page,
    create_position_page,
    update_position_page,
    employees_page,
    create_employee_page,
    update_employee_page,
)

from workers.api.views.positions import (
    get_positions,
    get_position,
    create_position,
    update_position,
    delete_position,
)

from workers.api.views.employees import (
    get_employee,
    get_employees,
    create_employee,
    update_employee,
    delete_employee,
)

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
