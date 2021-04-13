from django.urls import path

from dorm_launch_django.controls.views import (
    controls_update_view,
    controls_lottery_view,
)

app_name = "controls"
urlpatterns = [
    path("", view=controls_update_view, name='update'),
    path("~lottery/", view=controls_lottery_view, name='lottery'),
]
