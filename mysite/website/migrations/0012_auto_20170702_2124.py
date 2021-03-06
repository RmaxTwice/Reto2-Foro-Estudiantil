# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 01:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20170702_1759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solicitud',
            options={'verbose_name_plural': 'solicitudes'},
        ),
        migrations.RemoveField(
            model_name='materia',
            name='facultad',
        ),
        migrations.AddField(
            model_name='perfil',
            name='materia',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='website.Materia'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='estado',
            field=models.CharField(choices=[('L', 'Libre'), ('P', 'Pendiente'), ('A', 'Atendida')], default='L', max_length=1),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='escuela',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.Escuela'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='facultad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.Facultad'),
        ),
    ]
