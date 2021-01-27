# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-31 18:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180830_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operadorareatrabalho',
            options={'ordering': ['user'], 'verbose_name': 'Operador', 'verbose_name_plural': 'Operadores'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['first_name'], 'permissions': (('menu_dados_auxiliares', 'Mostrar menu de Dados auxiliares'), ('menu_tabelas_auxiliares', 'Mostrar menu de Tabelas auxiliares'), ('menu_contatos', 'Mostrar menu de de Contatos'), ('menu_grupocontatos', 'Mostrar menu de Grupos de Contatos'), ('menu_processos', 'Mostrar menu de Processos'), ('menu_area_trabalho', 'Mostrar menu de &Aacute;reas de trabalho'), ('menu_impresso_enderecamento', 'Mostrar menu de Impressos de endereçamento'), ('menu_relatorios', 'Mostrar Menu de Relatórios'))},
        ),
    ]