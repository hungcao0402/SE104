# Generated by Django 3.0.5 on 2022-05-27 08:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gara', '0015_auto_20220518_1645'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Staff',
        ),
    ]
