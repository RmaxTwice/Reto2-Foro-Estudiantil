# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20170701_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='escuela',
            name='facultad',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='website.Facultad'),
        ),
    ]