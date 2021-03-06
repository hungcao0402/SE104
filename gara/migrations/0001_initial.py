# Generated by Django 3.0.5 on 2022-05-01 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HieuXe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='PhieuTiepNhan',
            fields=[
                ('maphieutiepnhan', models.AutoField(primary_key=True, serialize=False)),
                ('tenchuxe', models.CharField(max_length=40)),
                ('bienso', models.PositiveIntegerField()),
                ('diachi', models.CharField(max_length=100)),
                ('dienthoai', models.PositiveIntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('hieuxe', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gara.HieuXe')),
            ],
        ),
    ]
