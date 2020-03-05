from django.db import models


class Producto(models.Model):
    EAN = models.CharField(max_length=13)
    cantidad = models.IntegerField()
    nombre = models.CharField(max_length=140)
    descipcion = models.CharField(max_length=140)

    def __str__(self):
        return "EAN:{0}, Producto:{1}, Cantidad:{2}, Descripcion:{3}".format(self.EAN, self.nombre, self.cantidad,
                                                                             self.descipcion)


class Pasillos(models.Model):
    n_pasillo = models.IntegerField()

    def __str__(self):
        return "Pasillo:{0}".format(self.n_pasillo)


class Estanterias(models.Model):
    pasillo = models.ForeignKey(Pasillos, on_delete=models.CASCADE, default=None)
    n_estanteria = models.IntegerField()

    def __str__(self):
        return "Pasillo:{0}, Estanteria:{1}".format(self.pasillo.n_pasillo, self.n_estanteria)


class localilizacionActualProd(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None)
    estanteria = models.ForeignKey(Estanterias, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "EAN:{0}, Producto:{1}, Pasillo:{2}, Estanteria:{3}".format(self.producto.EAN, self.producto.nombre,
                                                                           self.estanteria.pasillo,
                                                                           self.estanteria.n_estanteria)


class Almacen(models.Model):
    ubicacion = models.IntegerField()

    def __str__(self):
        return "Ubicacion:{0}".format(self.ubicacion)
