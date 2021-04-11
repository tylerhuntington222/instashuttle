from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms
from allauth.account.forms import SignupForm

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class CustomUserSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomUserSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user


class UserCreationForm(admin_forms.UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name")

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }
