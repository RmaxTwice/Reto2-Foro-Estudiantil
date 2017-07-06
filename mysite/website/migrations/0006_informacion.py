# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 17:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_escuela_facultad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('cuerpo', models.TextField(max_length=1000)),
                ('tema', models.CharField(choices=[('G', 'General'), ('T', 'Tesis'), ('S', 'Seminario'), ('SC', 'Servicio Comunitario'), ('P', 'Pasantías'), ('R', 'Reincorporaciones')], default='G', max_length=2)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_publicado', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha Publicado')),
                ('facultad', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='website.Facultad')),
            ],
        ),
    ]
