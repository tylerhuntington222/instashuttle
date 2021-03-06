from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from dorm_launch_django.users.api.views import UserViewSet
from dorm_launch_django.shuttles.api.views import ShuttleViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("shuttles", ShuttleViewSet)


app_name = "api"
urlpatterns = router.urls
