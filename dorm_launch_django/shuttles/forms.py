from django.contrib import admin
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from dorm_launch_django.shuttles.models import Shuttle
from django.forms import ModelForm, ValidationError
from django.forms.widgets import CheckboxSelectMultiple
from dorm_launch_django.shuttles.settings import MIN_PASSENGERS_TO_CREATE

class ShuttleCreateForm(ModelForm):
    class Meta:
        model = Shuttle
        fields = ['time_slot', 'destination', 'passengers']
        widgets = {
            'passengers': CheckboxSelectMultiple
        }

    def clean(self):
        data = self.cleaned_data
        print('DATA')
        print(data)
        err = f"""
            At least {MIN_PASSENGERS_TO_CREATE} passengers required
            to create a shuttle!
        """
        if 'passengers' in data:
            if len(data['passengers']) < MIN_PASSENGERS_TO_CREATE:
                raise ValidationError(err)
        raise ValidationError(err)


