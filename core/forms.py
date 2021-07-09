from django import forms
from django.forms import ModelForm
from .models import Producto
from .models import ProductoPC

class ProductoForm(ModelForm):

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
        labels = {
            'idProducto': 'Código producto',
            'descripcion': 'Descripción',
            'precio' : 'Precio Unitario $',
            'stock' : 'Stock',
            'imagen' : 'Imagen',
            'marca' : 'Marca'
        }
        widgets = {
            'idProducto' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'stock': forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'imagen': forms.FileInput(attrs={'class':'form-control'}),
            'marca': forms.Select(attrs={'class':'form-control'})
        }





class ProductoPcForm(ModelForm):

    class Meta:
        model = ProductoPC
        fields = [
            'idProductoPC',
            'descripcionPc',
            'precioPc',
            'stockPc',
            'imagenPc',
            
        ]
        labels = {
            'idProductoPC': 'codigo',
            'descripcionPc': 'descripcion',
            'precioPc' :'descripcion',
            'stockPc': 'precio',
            'imagenPc' :'imagen',
            
        }
        widgets = {
            'idProductoPC' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcionPc': forms.TextInput(attrs={'class':'form-control'}),
            'precioPc': forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'stockPc': forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'imagenPc': forms.FileInput(attrs={'class':'form-control'}),
            
        }     
    