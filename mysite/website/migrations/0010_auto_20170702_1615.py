# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 20:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20170702_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='supervisor',
        ),
        migrations.RemoveField(
            model_name='contacto',
            name='user',
        ),
        migrations.DeleteModel(
            name='Contacto',
        ),
    ]
