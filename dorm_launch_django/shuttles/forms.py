from dorm_launch_django.shuttles.models import Shuttle
from django.forms import ModelForm, ValidationError
from django.forms.widgets import CheckboxSelectMultiple
from dorm_launch_django.controls.models import Controls

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
        min_passengers = Controls.objects.first().min_passengers_for_request
        TOO_FEW_PASSENGERS_ERR = f"""
            At least {min_passengers} passengers required
            to request a shuttle!
        """
        # ensure that there are at least three passengers
        if 'passengers' not in data:
            raise ValidationError(TOO_FEW_PASSENGERS_ERR)
        if len(data['passengers']) < min_passengers:
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


class ShuttleUpdateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ShuttleUpdateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Shuttle
        fields = ['status', 'time_slot', 'destination', 'passengers']
        widgets = {
            'passengers': CheckboxSelectMultiple
        }

    def clean(self):
        data = self.cleaned_data
        min_passengers = Controls.objects.first().min_passengers_for_request
        TOO_FEW_PASSENGERS_ERR = f"""
            At least {min_passengers} passengers required
            to request a shuttle!
        """
        # ensure that there are at least three passengers
        if 'passengers' not in data:
            raise ValidationError(TOO_FEW_PASSENGERS_ERR)
        if len(data['passengers']) < min_passengers:
            raise ValidationError(TOO_FEW_PASSENGERS_ERR)

        # TODO: figure out how to handle this for passengers already on the
        # original shuttle
        # # check that user has enough tokens to create shuttle
        # for p in data['passengers']:
        #     if p.shuttle_tokens == 0:
        #         MAX_RESERVATIONS_ERR = f"""
        #             {p} is already signed up for the maximum number of shuttles!
        #             To reserve a spot for them on this shuttle,
        #             they must cancel an existing reservation.
        #         """
        #         raise ValidationError(MAX_RESERVATIONS_ERR)

