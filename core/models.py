from django.db import models

# Create your models here.

class Marca(models.Model):
    idMarca = models.IntegerField(primary_key=True, verbose_name='ID')
    marca = models.CharField(max_length=50,verbose_name='Marca')

    class Meta:
        verbose_name='marca'
        verbose_name_plural='marcas'
        ordering = ['marca']

    def __str__(self):
        return self.marca

class Producto(models.Model):
    idProducto = models.CharField(primary_key=True,max_length=10,verbose_name='ID')
    descripcion = models.CharField(max_length=100,verbose_name='Descripción')
    precio = models.IntegerField(verbose_name='Precio Unitario')
    stock = models.IntegerField(verbose_name='Stock')
    imagen = models.ImageField(verbose_name='Imagen',upload_to='productos',null=True,blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        ordering = ['descripcion']

    def __str__(self):
        return self.descripcion



#------------------------------------------------------------------------------------------------


class ProductoPC(models.Model):
    idProductoPC = models.CharField(primary_key=True,max_length=10,verbose_name='ID')
    descripcionPc = models.CharField(max_length=100,verbose_name='Descripción')
    precioPc = models.IntegerField(verbose_name='Precio Unitario')
    stockPc = models.IntegerField(verbose_name='Stock')
    imagenPc = models.ImageField(verbose_name='Imagen',upload_to='productos',null=True,blank=True)
  

    class Meta:
        verbose_name='productoPc'
        verbose_name_plural='productosPc'
        ordering = ['descripcionPc']

    def __str__(self):
        return self.descripcionPc

        