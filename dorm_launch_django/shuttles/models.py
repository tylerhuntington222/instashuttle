import uuid
from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, DateTimeField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Shuttle(Model):
    """Default user for dorm-launch-django."""

    uid = CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)

    campus_depart_location = CharField(_("Campus Departure Location"), blank=True, max_length=255, null=True)
    dropoff_location = CharField(_("Shuttle Dropoff Location"), blank=True, max_length=255, null=True)
    pickup_location = CharField(_("Shuttle Pickup Location"), blank=True, max_length=255, null=True)

    campus_depart_time = DateTimeField(_("Campus Departure Time"), blank=True, null=True)
    pickup_time = DateTimeField(_("Pickup Time"), blank=True, null=True)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("shuttles:detail", kwargs={"uid": self.uid})
