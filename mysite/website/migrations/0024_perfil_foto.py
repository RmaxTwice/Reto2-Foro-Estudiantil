# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_auto_20170726_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='foto',
            field=models.ImageField(default='media/user_avatars/default.gif', upload_to='user_avatars'),
        ),
    ]
