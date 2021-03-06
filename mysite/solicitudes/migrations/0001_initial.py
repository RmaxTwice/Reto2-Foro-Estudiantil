# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 19:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0023_auto_20170726_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('telefono', models.CharField(blank=True, default='', max_length=30)),
                ('titulo', models.CharField(max_length=125)),
                ('cuerpo', models.TextField(max_length=255)),
                ('fecha_enviado', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha Enviado')),
                ('estado', models.CharField(choices=[('Libre', 'Libre'), ('Pendiente', 'Pendiente'), ('Atendida', 'Atendida')], default='Libre', max_length=15)),
                ('tipo', models.CharField(choices=[('Asesoría', 'Asesoría'), ('Contacto', 'Contacto'), ('Sugerencia', 'Sugerencia')], default='Asesoría', max_length=15)),
                ('materia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Materia')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipiente', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'solicitudes',
            },
        ),
    ]
