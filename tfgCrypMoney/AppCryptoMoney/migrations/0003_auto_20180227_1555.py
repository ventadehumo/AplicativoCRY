# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-27 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppCryptoMoney', '0002_criptomoneda'),
    ]

    operations = [
        migrations.AddField(
            model_name='criptomoneda',
            name='percent_change_7d',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='criptomoneda',
            name='price_usd',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
