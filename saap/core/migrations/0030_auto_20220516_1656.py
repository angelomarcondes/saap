# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2022-05-16 19:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20220516_0935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['first_name'], 'permissions': (('menu_contatos', 'Mostrar menu de Contatos'), ('menu_processos', 'Mostrar menu de Processos'), ('menu_agenda', 'Mostrar menu de Agenda'), ('menu_correspondencias', 'Mostrar menu de Correspond&ecirc;ncias'), ('menu_sistema', 'Mostrar menu de Sistema'))},
        ),
    ]