from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Controls(models.Model):
    name = models.CharField(_("Name"), max_length=300, default='default')
    MIN_PASSENGERS_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
    ]
    min_passengers_for_request = models.IntegerField(
        _("Min. Passengers to Request Shuttle"),
        choices=MIN_PASSENGERS_CHOICES,
        default=3,
    )
    MAX_RESERVATIONS_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
    ]
    max_reservations_per_user = models.IntegerField(
        _('Max. Active Reservations per Student'),
        choices=MAX_RESERVATIONS_CHOICES,
        default=2,
    )


