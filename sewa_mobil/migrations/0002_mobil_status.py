# Generated by Django 3.1.1 on 2020-09-05 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sewa_mobil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobil',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], default='Available', max_length=20),
        ),
    ]
