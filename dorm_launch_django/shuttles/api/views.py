from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from dorm_launch_django.utils.api_authentication import TokenAuthWithQueryString

from dorm_launch_django.shuttles.api.serializers import ShuttleSerializer
from dorm_launch_django.shuttles.models import Shuttle

class ShuttleViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = ShuttleSerializer
    queryset = Shuttle.objects.all()
    lookup_field = "uid"
    authentication_classes = (TokenAuthWithQueryString,)

    def get_queryset(self, *args, **kwargs):
        return self.queryset
