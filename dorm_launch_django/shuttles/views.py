from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
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
from dorm_launch_django.shuttles.forms import (
    ShuttleCreateForm, ShuttleUpdateForm
)
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


class ShuttleList(LoginRequiredMixin, ListView):
  model = Shuttle

  def get_queryset(self):
      vis_statuses = ['Pending', 'Approved', 'Launched', 'Landed']
      qs = Shuttle.objects\
          .filter(status__in=vis_statuses)\
          .order_by('time_slot', 'status')
      return qs

shuttle_list_view = ShuttleList.as_view()


class ShuttleCreate(LoginRequiredMixin, CreateView):
    form_class = ShuttleCreateForm
    model = Shuttle

    def get_initial(self):
        user = self.request.user
        return {
            'request': self.request,
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
        if request.user.shuttle_tokens > 0:
            shuttle.passengers.add(request.user)
        else:
            err = """
                You are out of reservation tokens!
                You must cancel an existing reservation to join another shuttle.
            """
            messages.add_message(request, messages.ERROR, err)
        return redirect('shuttles:list')

shuttle_join_view = ShuttleJoinView.as_view()


class ShuttleApproveView(TemplateView, LoginRequiredMixin):
    template_name = 'shuttles/shuttle_list.html'

    def get(self, request, pk, *args, **kwargs):
        shuttle = Shuttle.objects.get(pk=pk)
        shuttle.status = 'Approved'
        shuttle.save()
        return redirect('shuttles:list')

shuttle_approve_view = ShuttleApproveView.as_view()

class ShuttleUnapproveView(TemplateView, LoginRequiredMixin):
    template_name = 'shuttles/shuttle_list.html'

    def get(self, request, pk, *args, **kwargs):
        shuttle = Shuttle.objects.get(pk=pk)
        shuttle.status = 'Pending'
        shuttle.save()
        return redirect('shuttles:list')

shuttle_unapprove_view = ShuttleUnapproveView.as_view()

class ShuttleDeleteView(TemplateView, LoginRequiredMixin):
    template_name = 'shuttles/shuttle_list.html'

    def get(self, request, pk, *args, **kwargs):
        shuttle = Shuttle.objects.get(pk=pk)
        shuttle.status = 'Deleted'
        shuttle.save()
        return redirect('shuttles:list')

shuttle_delete_view = ShuttleDeleteView.as_view()



class ShuttleUnJoinView(View, LoginRequiredMixin):
    template_name = 'shuttles/shuttle_list.html'

    def get(self, request, pk, *args, **kwargs):
        shuttle = Shuttle.objects.get(pk=pk)
        shuttle.passengers.remove(request.user)
        return redirect('shuttles:list')

shuttle_unjoin_view = ShuttleUnJoinView.as_view()


class ShuttleUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Shuttle
    template_name = 'shuttles/shuttle_update.html'
    success_message = _("Shuttle successfully updated!")
    form_class = ShuttleUpdateForm

    def get_context_data(self, *args, **kwargs):
        context = super(ShuttleUpdateView, self).get_context_data(*args, **kwargs)
        context['pk'] = str(self.get_object().pk)
        return context


    def get_success_url(self):
        return reverse_lazy('shuttles:list')

shuttle_update_view = ShuttleUpdateView.as_view()


class ShuttleRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse(
            "shuttles:detail",
            kwargs={"uid": self.request.shuttle.uid}
        )


shuttle_redirect_view = ShuttleRedirectView.as_view()
