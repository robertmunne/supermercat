from django.db import models

PRODUCT_STATUS = (
    ('E', 'Disponible'),
    ('D', 'No Disponiible')
)


class Producto(models.Model):
    EAN = models.CharField(max_length=13)
    cantidad = models.IntegerField()
    nombre = models.CharField(max_length=140, blank=True, null=True)
    descripcion = models.CharField(max_length=140)
    estado = models.CharField(max_length=1, null=False, default='E', choices=PRODUCT_STATUS)

    def __str__(self):
        return "EAN:{0}, Cantidad:{1}, Descripcion:{2}, estado:{3}".format(self.EAN, self.cantidad,
                                                                           self.descripcion, self.estado)


class Pasillos(models.Model):
    n_pasillo = models.IntegerField()

    def __str__(self):
        return "Pasillo:{0}".format(self.n_pasillo)


class Almacen(models.Model):
    ubicacion = models.IntegerField()

    def __str__(self):
        return "Ubicacion:{0}".format(self.ubicacion)


class Estanterias(models.Model):
    n_pasillo = models.ForeignKey(Pasillos, on_delete=models.CASCADE, default=None)
    n_estanteria = models.IntegerField()
    n_almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "Pasillo:{0}, Estanteria:{1}, ALmacen:{2}".format(self.n_pasillo.n_pasillo, self.n_estanteria,
                                                                 self.n_almacen)


class localilizacionActualProd(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None)
    estanteria = models.ForeignKey(Estanterias, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "Producto:{0}, Estanteria:{1}".format(self.producto.EAN, self.estanteria.n_estanteria)
