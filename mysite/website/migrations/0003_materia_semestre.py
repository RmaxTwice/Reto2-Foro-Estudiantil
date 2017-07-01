# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20170701_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='semestre',
            field=models.CharField(choices=[('electiva', 'Electiva'), ('1', 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV'), ('5', 'V'), ('6', 'VI'), ('7', 'VII'), ('8', 'VIII'), ('9', 'IX'), ('10', 'X')], default='I', max_length=10),
        ),
    ]
