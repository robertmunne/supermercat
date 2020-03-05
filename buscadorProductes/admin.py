# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
#admin.site.register(models.Restaurant)admin.site.register(models.Dish)

# Register your models here.
from buscadorProductes import models
admin.site.register(models.Producto)
admin.site.register(models.Pasillos)
admin.site.register(models.Estanterias)
admin.site.register(models.localilizacionActualProd)
admin.site.register(models.Almacen)
