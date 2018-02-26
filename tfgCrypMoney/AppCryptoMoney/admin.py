# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Usuario
from .models import Criptomoneda

admin.site.register(Usuario)
admin.site.register(Criptomoneda)
