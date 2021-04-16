from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, IntegerField, BooleanField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from dorm_launch_django.controls.models import Controls


class User(AbstractUser):
    """Default user for dorm_launch_django."""

    #: First and last name do not cover name patterns around the globe
    first_name = CharField(_("First Name"), blank=True, max_length=255)
    last_name = CharField(_("Last Name"), blank=True, max_length=255)
    is_test_user = BooleanField(_("Test User"), blank=True, default=False)

    @property
    def n_shuttles(self):
        return len(self.shuttle_set.all())

    @property
    def shuttle_tokens(self):
        max_res = Controls.objects.first().max_reservations_per_user
        return max_res - self.n_shuttles

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

