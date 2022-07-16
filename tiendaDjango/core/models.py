from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="id de categoria")
    nombreCategoria = models.CharField(max_length=80,verbose_name="nombre de la categoria")
    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="id de Producto")
    nombreProducto = models.CharField(max_length=80, verbose_name="nombre del Producto")
    valorProducto= models.IntegerField(verbose_name="valor del Producto")
    categoria =models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombreProducto