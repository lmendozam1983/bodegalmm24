from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del producto")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad en stock")
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio unitario")
    fecha_ingreso = models.DateField(auto_now_add=True, verbose_name="Fecha de ingreso")

    def __str__(self):
        return self.nombre


class Prestamo(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="prestamos_realizados")  # Usuario que realiza el préstamo
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name="prestamos_recibidos", null=True, blank=True) # Usuario que recibe el préstamo
    cantidad = models.PositiveIntegerField()
    fecha_prestamo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.producto.nombre} - {self.cantidad}"