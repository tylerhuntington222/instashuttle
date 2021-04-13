import random
from django.views.generic import TemplateView
from dorm_launch_django.shuttles.models import Shuttle
from django.shortcuts import render

class ControlsPanelView(TemplateView):
    template_name = 'controls/control_panel.html'

controls_panel_view = ControlsPanelView.as_view()

class ControlsLotteryView(TemplateView):
    template_name = 'controls/control_panel.html'

    def get(self, request, *args, **kwargs):
        pending = Shuttle.objects.filter(status='Pending')
        time_slots = list(set([s.time_slot for s in pending]))
        for ts in time_slots:
            shuttle_pool = Shuttle.objects.filter(time_slot=ts)
            random_shuttle = random.choice(shuttle_pool)
            random_shuttle.status = 'Approved'
            random_shuttle.save()
        context = {}
        return render(request, self.template_name, context=context)

controls_lottery_view = ControlsLotteryView.as_view()
