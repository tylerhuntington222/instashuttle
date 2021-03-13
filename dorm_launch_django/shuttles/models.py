import uuid
from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Shuttle(Model):
    """Default user for dorm-launch-django."""

    uid = CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)

    destination = CharField(_("Shuttle Destination"), blank=True, max_length=255)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("shuttles:detail", kwargs={"uid": self.uid})
