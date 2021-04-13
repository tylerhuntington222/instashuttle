from django.urls import path

from dorm_launch_django.controls.views import (
    controls_panel_view,
    controls_lottery_view,
)

app_name = "controls"
urlpatterns = [
    path("", view=controls_panel_view, name='panel'),
    path("~lottery/", view=controls_lottery_view, name='lottery'),
]
