# Generated by Django 4.0.4 on 2022-05-30 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gara', '0008_phieusuachua_tinhtrangthutien'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phieusuachua',
            name='tinhtrangthutien',
            field=models.IntegerField(default=0),
        ),
    ]
