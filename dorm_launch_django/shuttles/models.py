import uuid
from django.contrib.auth.models import AbstractUser
from django.db.models import (
    Model, CharField, DateTimeField, IntegerField, ManyToManyField,
    ForeignKey, CASCADE
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from dorm_launch_django.users.models import User


class Shuttle(Model):
    """Default user for dorm-launch-django."""


    STATUS_CHOICES = [
        ('Requested', 'Requested'),
        ('Approved', 'Approved'),
    ]
    status = CharField(
        _("Status"), blank=True, max_length=255, choices=STATUS_CHOICES,
        default='Requested'
    )
    campus_depart_location = CharField(_("Campus Departure Location"), blank=True, max_length=255, null=True)
    pickup_location = CharField(_("Shuttle Pickup Location"), blank=True, max_length=255, null=True)

    campus_depart_time = DateTimeField(_("Campus Departure Time"), blank=True, null=True)
    pickup_time = DateTimeField(_("Pickup Time"), blank=True, null=True)
    return_time = DateTimeField(_("Return Time"), blank=True, null=True)
    capacity = IntegerField(_("Capacity"), blank=True, default=9)

    created_by = ForeignKey(
        User, related_name='creator', blank=True, null=True, on_delete=CASCADE
    )
    passengers = ManyToManyField(User)

    DESTINATION_CHOICES = [
        ('San Ramon Safeway', 'San Ramon Safeway'),
        ("San Ramon Trader Joe's", "San Ramon Trader Joe's"),
        ("Danville Trader Joe's", "Danville Trader Joe's"),
        ("San Ramon Sharetea", "San Ramon Sharetea"),
    ]

    destination = CharField(
        _("Destination"),
        max_length=255,
        choices=DESTINATION_CHOICES,
    )

    TIME_SLOT_CHOICES = [
        # ('Friday 7:00-9:00', 'Friday 7:00-9:00'),
        # ('Saturday 11:30-1:30', 'Saturday 11:30-1:30'),
        # ('Saturday 2:00-4:00', 'Saturday 2:00-4:00'),
        # ('Saturday 7:00-9:00', 'Saturday 7:00-9:00'),
        ('0', 'Friday 7:00-9:00'),
        ('1', 'Saturday 11:30-1:30'),
        ('2', 'Saturday 2:00-4:00'),
        ('3', 'Saturday 7:00-9:00'),
    ]
    time_slot = CharField(
        _("Time Slot"),
        max_length=300,
        choices=TIME_SLOT_CHOICES,
    )

    @property
    def open_seats(self):
        return self.capacity - len(self.passengers.all())

    @property
    def passenger_usernames(self):
        return [p.username for p in self.passengers.all()]

    # @property
    # def time_slot_index(self):
    #     """
    #     Zero-based index of the shuttle time slot
    #     :return:
    #     """
    #     indices = {
    #         'Friday 7:00-9:00': 0,
    #         'Saturday 11:30-1:30': 1,
    #         'Saturday 2:00-4:00': 2,
    #         'Saturday 7:00-9:00': 3
    #     }
    #     return indices[self.time_slot]

    @property
    def time_slot_str(self):
        """
        Human-readable string of the shuttle time slot
        :return:
        """
        return self.get_time_slot_display()


    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("shuttles:detail", kwargs={"pk": self.pk})
