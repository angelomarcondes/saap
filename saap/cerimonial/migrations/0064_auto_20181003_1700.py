# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-10-03 20:00
from __future__ import unicode_literals

from django.db import migrations
import exclusivebooleanfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cerimonial', '0063_auto_20181003_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='permite_contato',
            field=exclusivebooleanfield.fields.ExclusiveBooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, help_text="Escolhido para contato do gabinete.                    Se estiver 'Sim', após você salvar, este passa a ser o escolhido, alterando o atual", on=('contato',), verbose_name='Contato'),
        ),
        migrations.AlterField(
            model_name='email',
            name='principal',
            field=exclusivebooleanfield.fields.ExclusiveBooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, help_text="Se estiver 'Sim', após você salvar, este passa a ser o principal, alterando o atual", on=('contato',), verbose_name='Principal?'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='permite_contato',
            field=exclusivebooleanfield.fields.ExclusiveBooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, help_text="Escolhido para contato do gabinete.                    Se estiver 'Sim', após você salvar, este passa a ser o escolhido, alterando o atual", on=('contato',), verbose_name='Contato'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='principal',
            field=exclusivebooleanfield.fields.ExclusiveBooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, help_text="Se estiver 'Sim', após você salvar, este passa a ser o principal, alterando o atual", on=('contato',), verbose_name='Principal?'),
        ),
        migrations.AlterField(
            model_name='localtrabalho',
            name='principal',
            field=exclusivebooleanfield.fields.ExclusiveBooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, help_text="Se estiver 'Sim', após você salvar, este passa a ser o principal, alterando o atual", on=('contato',), verbose_name='Principal?'),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='permite_contato',
            field=exclusivebooleanfield.fields.ExclusiveBooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, help_text="Escolhido para contato do gabinete.                    Se estiver 'Sim', após você salvar, este passa a ser o escolhido, alterando o atual", on=('contato',), verbose_name='Contato'),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='principal',
            field=exclusivebooleanfield.fields.ExclusiveBooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, help_text="Se estiver 'Sim', após você salvar, este passa a ser o principal, alterando o atual", on=('contato',), verbose_name='Principal?'),
        ),
    ]