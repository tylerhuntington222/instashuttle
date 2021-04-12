from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, IntegerField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from dorm_launch_django.shuttles.settings import MAX_SHUTTLE_RES_PER_USER


class User(AbstractUser):
    """Default user for dorm_launch_django."""

    #: First and last name do not cover name patterns around the globe
    first_name = CharField(_("First Name"), blank=True, max_length=255)
    last_name = CharField(_("Last Name"), blank=True, max_length=255)

    @property
    def n_shuttles(self):
        return len(self.shuttle_set.all())

    @property
    def shuttle_tokens(self):
        return MAX_SHUTTLE_RES_PER_USER - self.n_shuttles

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

