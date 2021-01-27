# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-10-03 17:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cerimonial', '0059_auto_20181003_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='permite_contato',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, help_text='Autorizado para contato do gabinete', verbose_name='Contato'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='permite_contato',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, help_text='Autorizado para contato do gabinete', verbose_name='Contato'),
        ),
        migrations.AddField(
            model_name='telefone',
            name='permite_contato',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, help_text='Autorizado para contato do gabinete', verbose_name='Contato'),
        ),
        migrations.AlterField(
            model_name='email',
            name='contato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_set', to='cerimonial.Contato', verbose_name='Contato'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='contato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco_set', to='cerimonial.Contato', verbose_name='Contato'),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='contato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefone_set', to='cerimonial.Contato', verbose_name='Contato'),
        ),
    ]