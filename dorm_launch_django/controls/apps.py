from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ControlsConfig(AppConfig):
    name = "dorm_launch_django.controls"
    verbose_name = _("Controls")

    def ready(self):
        try:
            import dorm_launch_django.users.signals  # noqa F401
        except ImportError:
            pass
