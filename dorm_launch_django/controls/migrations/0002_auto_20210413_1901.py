# Generated by Django 3.1.7 on 2021-04-13 18:48

from django.db import migrations
from dorm_launch_django.controls.models import Controls
from django.conf import settings

from django.db import migrations

def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Controls = apps.get_model("controls", "Controls")
    db_alias = schema_editor.connection.alias
    Controls.objects.using(db_alias).create(
            min_passengers_for_request=settings.MIN_PASSENGERS_FOR_REQUEST,
            max_reservations_per_user=settings.MAX_RESERVATIONS_PER_USER
    )

def reverse_func(apps, schema_editor):
    # forwards_func() creates an initial Controls instance
    # so reverse_func() should delete it.
    Controls = apps.get_model("controls", "Controls")
    db_alias = schema_editor.connection.alias
    Controls.objects.using(db_alias).filter(name="default").delete()



class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]