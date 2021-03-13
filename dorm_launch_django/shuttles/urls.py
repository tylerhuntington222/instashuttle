from django.urls import path

from dorm_launch_django.shuttles.views import (
    shuttle_detail_view,
    shuttle_redirect_view,
    shuttle_update_view,
)

app_name = "shuttles"
urlpatterns = [
    path("~redirect/", view=shuttle_redirect_view, name="redirect"),
    path("~update/", view=shuttle_update_view, name="update"),
    path("<str:username>/", view=shuttle_detail_view, name="detail"),
]
