# Generated by Django 3.1.1 on 2020-10-02 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa_mobil', '0012_pesanan_denda'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobil',
            name='rating',
            field=models.IntegerField(blank=True, default=5),
            preserve_default=False,
        ),
    ]