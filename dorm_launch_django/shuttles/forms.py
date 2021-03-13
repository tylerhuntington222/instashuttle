from django.contrib import admin
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from dorm_launch_django.shuttles.models import Shuttle

admin.site.register(Shuttle)

# class ShuttleChangeForm(admin_forms.UserChangeForm):
#     class Meta(admin_forms.UserChangeForm.Meta):
#         model = User
#
#
# class UserCreationForm(admin_forms.UserCreationForm):
#     class Meta(admin_forms.UserCreationForm.Meta):
#         model = User
#
#         error_messages = {
#             "username": {"unique": _("This username has already been taken.")}
#         }
