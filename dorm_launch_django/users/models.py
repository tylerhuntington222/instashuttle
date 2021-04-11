from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, IntegerField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for dorm_launch_django."""

    #: First and last name do not cover name patterns around the globe
    first_name = CharField(_("First Name"), blank=True, max_length=255)
    last_name = CharField(_("Last Name"), blank=True, max_length=255)
    shuttle_tokens = IntegerField(_("Shuttle Tokens"), blank=True, default=0)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

