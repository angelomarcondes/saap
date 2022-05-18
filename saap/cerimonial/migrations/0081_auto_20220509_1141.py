# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2022-05-09 14:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cerimonial', '0080_auto_20201203_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criação'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificação'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modificador'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Criador'),
        ),
        migrations.AlterField(
            model_name='dependente',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criação'),
        ),
        migrations.AlterField(
            model_name='dependente',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificação'),
        ),
        migrations.AlterField(
            model_name='dependente',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modificador'),
        ),
        migrations.AlterField(
            model_name='dependente',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Criador'),
        ),
        migrations.AlterField(
            model_name='email',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criação'),
        ),
        migrations.AlterField(
            model_name='email',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificação'),
        ),
        migrations.AlterField(
            model_name='email',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modificador'),
        ),
        migrations.AlterField(
            model_name='email',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Criador'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criação'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificação'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modificador'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Criador'),
        ),
        migrations.AlterField(
            model_name='filiacaopartidaria',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criação'),
        ),
        migrations.AlterField(
            model_name='filiacaopartidaria',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificação'),
        ),
        migrations.AlterField(
            model_name='filiacaopartidaria',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modificador'),
        ),
        migrations.AlterField(
            model_name='filiacaopartidaria',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Criador'),
        ),
        migrations.AlterField(
            model_name='grupodecontatos',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criação'),
        ),
        migrations.AlterField(
            model_name='grupodecontatos',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificação'),
        ),
        migrations.AlterField(
            model_name='grupodecontatos',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modificador'),
        ),
        migrations.AlterField(
            model_name='grupodecontatos',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Criador'),
        ),
        migrations.AlterField(
            model_name='localtrabalho',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criação'),
        ),
        migrations.AlterField(
            model_name='localtrabalho',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificação'),
        ),
        migrations.AlterField(
            model_name='localtrabalho',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modificador'),
        ),
        migrations.AlterField(
            model_name='localtrabalho',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Criador'),
        ),
        migrations.AlterField(
            model_name='processo',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criação'),
        ),
        migrations.AlterField(
            model_name='processo',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificação'),
        ),
        migrations.AlterField(
            model_name='processo',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modificador'),
        ),
        migrations.AlterField(
            model_name='processo',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Criador'),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criação'),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificação'),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modificador'),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Criador'),
        ),
    ]
