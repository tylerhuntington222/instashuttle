from django.urls import path

from dorm_launch_django.shuttles.views import (
    shuttle_detail_view,
    shuttle_redirect_view,
    shuttle_update_view,
    shuttle_join_view,
    shuttle_unjoin_view,
    shuttle_create_view,
    shuttle_list_view,
)

app_name = "shuttles"
urlpatterns = [
    path("", view=shuttle_list_view, name='list'),
    path("~create/", view=shuttle_create_view, name="create"),
    path("~redirect/", view=shuttle_redirect_view, name="redirect"),
    path("~update/", view=shuttle_update_view, name="update"),
    path("~join/<int:pk>/", view=shuttle_join_view, name="join"),
    path("~unjoin/<int:pk>/", view=shuttle_unjoin_view, name="unjoin"),
    path("<int:pk>/", view=shuttle_detail_view, name="detail"),
]
