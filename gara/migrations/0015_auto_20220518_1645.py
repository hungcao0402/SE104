# Generated by Django 3.0.5 on 2022-05-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gara', '0014_auto_20220518_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='emails',
            field=models.EmailField(default='anonymous@gmail.com', max_length=90, null=True),
        ),
    ]