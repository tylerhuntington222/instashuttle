import random
from django.views.generic import TemplateView
from dorm_launch_django.shuttles.models import Shuttle
from dorm_launch_django.controls.models import Controls
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import UpdateView
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect, reverse


class ControlsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Controls
    fields = ["min_passengers_for_request", "max_reservations_per_user"]
    success_message = _("Settings successfully updated!")

    def get_object(self):
        return Controls.objects.get(name='default')

    def get_success_url(self):
        return reverse('controls:update')


controls_update_view = ControlsUpdateView.as_view()


class ControlsLotteryView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'controls/controls_form.html'
    err_message = ""
    success_message = _(
        "Lottery complete! "
        "Check the Dashboard to view updated status of each shuttle."
    )

    def get(self, request, *args, **kwargs):
        shuttles = Shuttle.objects.all()
        time_slots = list(set([s.time_slot for s in shuttles]))
        for ts in time_slots:
            shuttle_pool = Shuttle.objects.filter(time_slot=ts)
            # init counter for number of shuttles approved for a time slot
            n_approved_for_slot = 0
            # check for already approved shuttles in this time slot
            for s in shuttle_pool:
                if s.status == 'Approved':
                    n_approved_for_slot += 1
            # handle case of time slot for which at least one shuttle has
            # already been approved
            if n_approved_for_slot > 1:
                # Handle case of time slot for which multiple shuttles approved.
                # We compute minimum number of conflicting approved shuttles
                # for this time slot that need to be mannually unapproved
                # a render a corresponding error message in the template.
                n_unnaprove = str(n_approved_for_slot - 1)
                print(n_unnaprove)
                self.err_message = _(
                    "Error running lottery! Multiple shuttles have already "
                    "been approved for %(time_slot)s. "
                    "Resolve this issue by manually unapproving at "
                    "least %(n_u)s of these on the Dashboard, then re-run "
                    "the lottery."
                ) % {'time_slot': s.time_slot_str, 'n_u': n_unnaprove}
                continue
            # Handle the case where exactly one shuttle has already been
            # approved for the current time slot. Here, we just continue
            # to the next iteration of the loop (i.e. the next time slot),
            # bypassing the random selection of a shuttle to approve.
            if n_approved_for_slot == 1:
                continue
            # Lastly, handle the case where no shuttles have been approved
            # for the current time slot yet so we need to randomly select one
            # and update its status to "Approved"
            random_shuttle = random.choice(shuttle_pool)
            random_shuttle.status = 'Approved'
            random_shuttle.save()
        if self.err_message:
            messages.add_message(request, messages.ERROR, self.err_message)
        else:
            messages.add_message(request, messages.SUCCESS, self.success_message)
        return redirect('controls:update')


controls_lottery_view = ControlsLotteryView.as_view()
