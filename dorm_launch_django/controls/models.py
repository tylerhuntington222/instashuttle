from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Controls(models.Model):
    name = models.CharField(_("Name"), max_length=300, default='default')
    min_passengers_for_request = models.IntegerField(
        _("Min. Passengers to Request Shuttle"), default=3
    )
    max_reservations_per_user = models.IntegerField(
        _('Max. Active Reservations Per Student'), default=2
    )


