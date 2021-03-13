from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ShuttlesConfig(AppConfig):
    name = "dorm_launch_django.shuttles"
    verbose_name = _("Shuttles")

    def ready(self):
        try:
            import dorm_launch_django.users.signals  # noqa F401
        except ImportError:
            pass
