from dorm_launch_django.models import Shuttle
from rest_framework import serializers

class ShuttleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shuttle
        fields = ["uid", "destination", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:shuttle-detail", "lookup_field": "uid"}
        }
