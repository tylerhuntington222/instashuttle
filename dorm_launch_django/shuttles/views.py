from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from dorm_launch_django.shuttles.models import Shuttle



class ShuttleDetailView(LoginRequiredMixin, DetailView):

    model = Shuttle


shuttle_detail_view = ShuttleDetailView.as_view()


class ShuttleUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Shuttle
    fields = ["destination"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return self.request.shuttle.get_absolute_url()  # type: ignore [union-attr]

    def get_object(self):
        return self.request.shuttle


shuttle_update_view = ShuttleUpdateView.as_view()


class ShuttleRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("shuttles:detail", kwargs={"uid": self.request.shuttle.uid})


shuttle_redirect_view = UserRedirectView.as_view()
