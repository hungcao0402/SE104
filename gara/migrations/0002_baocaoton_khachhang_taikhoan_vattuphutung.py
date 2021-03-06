# Generated by Django 3.0.5 on 2022-05-10 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gara', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KhachHang',
            fields=[
                ('makhachhang', models.AutoField(primary_key=True, serialize=False)),
                ('tenchuxe', models.CharField(max_length=40)),
                ('diachi', models.CharField(max_length=100)),
                ('dienthoai', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TaiKhoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenTaiKhoan', models.CharField(max_length=10)),
                ('MatKhau', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='vattuphutung',
            fields=[
                ('mavattuphutrung', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(max_length=40)),
                ('soluong', models.PositiveIntegerField()),
                ('dongia', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='baocaoton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TonDau', models.PositiveIntegerField()),
                ('PhatSinh', models.PositiveIntegerField()),
                ('TonCuoi', models.PositiveIntegerField()),
                ('thang', models.DateField()),
                ('MaPhuTung', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gara.vattuphutung')),
            ],
        ),
    ]
