from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            'idProducto',
            'descripcion',
            'precio',
            'stock',
            'imagen',
            'marca'
        ]
