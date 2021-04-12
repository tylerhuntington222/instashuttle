from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    DetailView, RedirectView, UpdateView, CreateView, TemplateView, View
)
from dorm_launch_django.users.models import User
from dorm_launch_django.shuttles.models import Shuttle
from django.views.generic import ListView, FormView
from django.utils import timezone
from django.forms.widgets import CheckboxSelectMultiple
from dorm_launch_django.shuttles.forms import ShuttleCreateForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


class ShuttleList(LoginRequiredMixin, ListView):
  model = Shuttle

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['now'] = timezone.now()
      return context

shuttle_list_view = ShuttleList.as_view()


class ShuttleCreate(CreateView):
    form_class = ShuttleCreateForm
    model = Shuttle

    def get_initial(self):
        user = self.request.user
        return {
            'passengers': user
        }

    def get_success_url(self):
        return reverse_lazy('shuttles:list')

shuttle_create_view = ShuttleCreate.as_view()

class ShuttleDetailView(LoginRequiredMixin, DetailView):
    model = Shuttle

shuttle_detail_view = ShuttleDetailView.as_view()


class ShuttleJoinView(TemplateView, LoginRequiredMixin):
    template_name = 'shuttles/shuttle_list.html'

    def get(self, request, pk, *args, **kwargs):
        shuttle = Shuttle.objects.get(pk=pk)
        err=""
        if request.user.shuttle_tokens > 0:
            shuttle.passengers.add(request.user)
        else:
            err = 'You cannot join any more shuttles!'
        context = {
            'object_list': Shuttle.objects.all(),
            'err': err
        }
        return render(request, self.template_name, context=context)

shuttle_join_view = ShuttleJoinView.as_view()

class ShuttleUnJoinView(View, LoginRequiredMixin):
    template_name = 'shuttles/shuttle_list.html'

    def get(self, request, pk, *args, **kwargs):
        shuttle = Shuttle.objects.get(pk=pk)
        shuttle.passengers.remove(request.user)
        return redirect('shuttles:list')

shuttle_unjoin_view = ShuttleUnJoinView.as_view()


class ShuttleUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Shuttle
    fields = ["destination"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return self.request.shuttle.get_absolute_url()

    def get_object(self):
        return self.request.shuttle


shuttle_update_view = ShuttleUpdateView.as_view()


class ShuttleRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("shuttles:detail", kwargs={"uid": self.request.shuttle.uid})


shuttle_redirect_view = ShuttleRedirectView.as_view()
