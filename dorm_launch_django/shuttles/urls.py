from django.urls import path

from dorm_launch_django.shuttles.views import (
    shuttle_detail_view,
    shuttle_redirect_view,
    shuttle_update_view,
    shuttle_join_view,
    shuttle_unjoin_view,
    shuttle_create_view,
    shuttle_list_view,
    shuttle_approve_view,
    shuttle_unapprove_view,
    shuttle_delete_view,
)

app_name = "shuttles"
urlpatterns = [
    path("", view=shuttle_list_view, name='list'),
    path("~create/", view=shuttle_create_view, name="create"),
    path("~redirect/", view=shuttle_redirect_view, name="redirect"),
    path("~update/<int:pk>/", view=shuttle_update_view, name="update"),
    path("~join/<int:pk>/", view=shuttle_join_view, name="join"),
    path("~unjoin/<int:pk>/", view=shuttle_unjoin_view, name="unjoin"),
    path("~approve/<int:pk>/", view=shuttle_approve_view, name="approve"),
    path("~unapprove/<int:pk>/", view=shuttle_unapprove_view, name="unapprove"),
    path("~delete/<int:pk>/", view=shuttle_delete_view, name="delete"),
    path("<int:pk>/", view=shuttle_detail_view, name="detail"),
]
