# Generated by Django 3.1.2 on 2020-12-02 13:51

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geolocation', '0002_auto_20201202_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326, verbose_name='موقعیت جغرافیایی'),
        ),
    ]