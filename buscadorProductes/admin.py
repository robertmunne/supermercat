# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Producto

# Register your models here.
from buscadorProductes import models


# admin.site.register(models.Producto)
@admin.register(Producto)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('EAN', 'nombre', 'cantidad', 'descripcion', 'estado')
    list_editable = ('estado', 'cantidad',)


admin.site.register(models.Pasillos)
admin.site.register(models.Estanterias)
admin.site.register(models.localilizacionActualProd)
admin.site.register(models.Almacen)
