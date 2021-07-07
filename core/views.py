from django.shortcuts import render
from core import models
from .models import Producto
from core import forms
from .forms import ProductoForm
# Create your views here.

def home(request):
    productos = Producto.objects.all()
    return render(request,"core/product-list.html",{'productos':productos})




def add(request):
    add_producto = ProductoForm
    return render (request,"core/product-new",{'form':add_producto})
     


    