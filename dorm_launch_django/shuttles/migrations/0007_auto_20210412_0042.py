# Generated by Django 3.1.7 on 2021-04-12 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuttles', '0006_auto_20210412_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shuttle',
            name='time_slot',
            field=models.CharField(choices=[('Friday 7:00-9:00', 'Friday 7:00-9:00'), ('Saturday 11:30-1:30', 'Saturday 11:30-1:30'), ('Saturday 2:00-4:00', 'Saturday 2:00-4:00'), ('Saturday 7:00-9:00', 'Saturday 7:00-9:00')], default='fri_7_9', max_length=200),
        ),
    ]
