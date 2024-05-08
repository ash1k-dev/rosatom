from django.conf.urls import url

app_name = "workers"

from workers.views import (
    positions_page,
    create_position_page,
    update_position_page,
)

from workers.api.views.positions import (
    get_positions,
    get_position,
    create_position,
    update_position,
    delete_position,
)

urlpatterns = [
    # api
    url(r"^api/get-positions/$", get_positions),
    url(r"^api/get-position/(?P<position_id>\d+)/$", get_position),
    url(r"^api/create-position/$", create_position),
    url(r"^api/update-position/$", update_position),
    url(r"^api/delete-position/$", delete_position),
    # views
    url(r"^positions/(?P<position_id>\d+)/$", update_position_page),
    url(r"^positions/$", positions_page),
    url(r"^positions/create/$", create_position_page),
]
