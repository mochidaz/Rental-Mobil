# Generated by Django 3.1.1 on 2020-09-15 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa_mobil', '0008_auto_20200915_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesanan',
            name='waktu_ambil',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='pesanan',
            name='waktu_kembali',
            field=models.DateField(),
        ),
    ]