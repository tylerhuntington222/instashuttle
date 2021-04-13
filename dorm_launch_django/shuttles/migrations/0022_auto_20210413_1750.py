# Generated by Django 3.1.7 on 2021-04-13 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuttles', '0021_auto_20210413_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shuttle',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Launched', 'Launched')], default='Pending', max_length=255, verbose_name='Status'),
        ),
    ]
