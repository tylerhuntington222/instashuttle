from django.contrib import admin
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from dorm_launch_django.shuttles.models import Shuttle
from django.forms import ModelForm, ValidationError
from django.forms.widgets import CheckboxSelectMultiple
from dorm_launch_django.shuttles.settings import MIN_PASSENGERS_TO_CREATE

class ShuttleCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ShuttleCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Shuttle
        fields = ['time_slot', 'destination', 'passengers']
        widgets = {
            'passengers': CheckboxSelectMultiple
        }

    def clean(self):
        data = self.cleaned_data
        TOO_FEW_PASSENGERS_ERR = f"""
            At least {MIN_PASSENGERS_TO_CREATE} passengers required
            to request a shuttle!
        """
        # ensure that there are at least three passengers
        if 'passengers' not in data:
            raise ValidationError(TOO_FEW_PASSENGERS_ERR)
        if len(data['passengers']) < MIN_PASSENGERS_TO_CREATE:
            raise ValidationError(TOO_FEW_PASSENGERS_ERR)

        # check that user has enough tokens to create shuttle
        for p in data['passengers']:
            if p.shuttle_tokens == 0:
                MAX_RESERVATIONS_ERR = f"""
                    {p} is already signed up for the maximum number of shuttles!
                    To reserve a spot for them on this shuttle,
                    they must cancel an existing reservation.
                """
                raise ValidationError(MAX_RESERVATIONS_ERR)
