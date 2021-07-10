from django import forms
from django.forms import ModelForm

from .models import ProductoPC


   
class ProductoPcForm(ModelForm):

    class Meta:
        Model = ProductoPC
        fields = [
            'idProductoPc'
            'descripcionPc',
            'precioPc',
            'stockPc',
            'imagenPc',
            ]



        labels = {
            'idProductoPc': 'Código producto',
            'descripcionPc': 'Descripción',
            'precioPc' : 'Precio Unitario $',
            'stockPc' : 'Stock',
            'imagenPc' : 'Imagen',
       
        }
        widgets = {
            'idProductoPc' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcionPc': forms.TextInput(attrs={'class':'form-control'}),
            'precioPc': forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'stockPc': forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'imagenPc': forms.FileInput(attrs={'class':'form-control'}),
           
        } 

  