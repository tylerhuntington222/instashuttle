# Generated by Django 3.1.7 on 2021-04-12 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuttles', '0013_auto_20210412_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shuttle',
            name='destination',
            field=models.CharField(choices=[('San Ramon Safeway', 'San Ramon Safeway'), ("San Ramon Trader Joe's", "San Ramon Trader Joe's"), ("Danville Trader Joe's", "Danville Trader Joe's"), ('San Ramon Sharetea', 'San Ramon Sharetea')], default='San Ramon Safeway', max_length=255, verbose_name='Destination'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shuttle',
            name='time_slot',
            field=models.CharField(choices=[('Friday 7:00-9:00', 'Friday 7:00-9:00'), ('Saturday 11:30-1:30', 'Saturday 11:30-1:30'), ('Saturday 2:00-4:00', 'Saturday 2:00-4:00'), ('Saturday 7:00-9:00', 'Saturday 7:00-9:00')], max_length=200, verbose_name='Time Slot'),
        ),
    ]
