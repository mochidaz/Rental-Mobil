# Generated by Django 3.1.1 on 2020-09-11 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa_mobil', '0002_mobil_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobil',
            name='transmisi',
            field=models.CharField(choices=[('Auto', 'Auto'), ('Manual', 'Manual')], default='Manual', max_length=10),
        ),
    ]
