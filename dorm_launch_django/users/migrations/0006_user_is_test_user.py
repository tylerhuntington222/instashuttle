# Generated by Django 3.1.7 on 2021-04-16 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_shuttle_tokens'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_test_user',
            field=models.BooleanField(blank=True, null=True, verbose_name='Test User'),
        ),
    ]