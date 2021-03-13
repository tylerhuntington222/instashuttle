from dorm_launch_django.shuttles import Shuttle

from config import celery_app

@celery_app.task()
def get_shuttles_count():
    """A pointless Celery task to demonstrate usage."""
    return Shuttle.objects.count()
