# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2022-05-11 18:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20210218_1356'),
        ('cerimonial', '0085_auto_20220511_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='workspace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.AreaTrabalho', verbose_name='Área de trabalho'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 11, 18, 53, 55, 797120, tzinfo=utc), verbose_name='Término'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 11, 18, 53, 55, 797033, tzinfo=utc), verbose_name='Início'),
        ),
    ]