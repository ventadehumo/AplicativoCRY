# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-24 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCryptoMoney', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criptomoneda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_Criptomoneda', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('symbol', models.CharField(max_length=200)),
                ('rank', models.CharField(max_length=200)),
                ('_24h_volume_usd', models.CharField(max_length=200)),
                ('market_cap_usd', models.CharField(max_length=200)),
                ('available_supply', models.CharField(max_length=200)),
                ('total_supply', models.CharField(max_length=200)),
                ('max_supply', models.CharField(max_length=200)),
                ('percent_change_1h', models.CharField(max_length=200)),
                ('percent_change_24h', models.CharField(max_length=200)),
                ('last_updated', models.CharField(max_length=200)),
            ],
        ),
    ]
