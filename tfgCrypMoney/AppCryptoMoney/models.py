# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Instance corporate.
class Usuario(models.Model):
    UserName = models.CharField(max_length=200)
    UserId = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    UserKey = models.CharField(max_length=200)
    GroupName = models.CharField(max_length=200)
    Monedas = models.CharField(max_length=200)

    def __str__(self):
        return self.UserName

class Criptomoneda (models.Model):
    id_Criptomoneda = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=200)
    rank = models.CharField(max_length=200)
    _24h_volume_usd = models.CharField(max_length=200)
    market_cap_usd = models.CharField(max_length=200)
    available_supply = models.CharField(max_length=200)
    total_supply = models.CharField(max_length=200)
    max_supply = models.CharField(max_length=200)
    percent_change_1h = models.CharField(max_length=200)
    percent_change_24h = models.CharField(max_length=200)
    last_updated = models.CharField(max_length=200)

    def __str__(self):
        return self.UserName