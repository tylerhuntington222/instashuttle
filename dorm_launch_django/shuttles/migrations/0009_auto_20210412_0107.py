# Generated by Django 3.1.7 on 2021-04-12 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuttles', '0008_auto_20210412_0049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shuttle',
            name='open_seats',
        ),
        migrations.AddField(
            model_name='shuttle',
            name='capacity',
            field=models.IntegerField(blank=True, default=9, verbose_name='Capacity'),
        ),
    ]
