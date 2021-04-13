import random
from django.views.generic import TemplateView
from dorm_launch_django.shuttles.models import Shuttle
from dorm_launch_django.controls.models import Controls
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect, reverse


class ControlsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Controls
    fields = ["min_passengers_for_request", "max_reservations_per_user"]
    success_message = _("Settings successfully updated")


    def get_success_url(self):
        return reverse('controls:update')

    def get_object(self):
        return Controls.objects.get(name='default')


controls_update_view = ControlsUpdateView.as_view()

# class ControlsPanelView(LoginRequiredMixin, TemplateView):
#     template_name = 'controls/controls_form.html'
#     def get(self, request, *args, **kwargs):
#
#         context = {
#             'controls': Controls.objects.get(name='default')
#         }
#         return render(request, self.template_name, context=context)
#
# controls_panel_view = ControlsPanelView.as_view()

class ControlsLotteryView(TemplateView):
    template_name = 'controls/controls_form.html'

    def get(self, request, *args, **kwargs):
        pending = Shuttle.objects.filter(status='Pending')
        time_slots = list(set([s.time_slot for s in pending]))
        for ts in time_slots:
            shuttle_pool = Shuttle.objects.filter(time_slot=ts)
            random_shuttle = random.choice(shuttle_pool)
            random_shuttle.status = 'Approved'
            random_shuttle.save()
        return redirect('controls:update')

controls_lottery_view = ControlsLotteryView.as_view()
