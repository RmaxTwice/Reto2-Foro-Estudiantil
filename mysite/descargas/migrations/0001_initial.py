# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website', '0020_auto_20170720_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descarga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('G', 'Guia'), ('E', 'Exámen'), ('L', 'Laboratorio'), ('B', 'Libro')], default='G', max_length=1)),
                ('fecha_publicado', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha Publicado')),
                ('materia', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='website.Materia')),
            ],
        ),
    ]