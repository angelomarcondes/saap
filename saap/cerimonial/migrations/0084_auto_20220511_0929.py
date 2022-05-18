# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2022-05-11 12:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerimonial', '0083_auto_20220510_1409'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evento',
            options={},
        ),
        migrations.RemoveField(
            model_name='evento',
            name='data_fim',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='data_inicio',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='hora_fim',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='hora_inicio',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='localizacao',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='observacoes',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='titulo',
        ),
        migrations.AddField(
            model_name='evento',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='evento',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='evento',
            name='location',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='evento',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='evento',
            name='title',
            field=models.CharField(default='Evento', max_length=200),
        ),
    ]
