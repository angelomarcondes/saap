# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-11-01 18:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20181001_1728'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bairro',
            unique_together=set([('nome', 'municipio')]),
        ),
    ]