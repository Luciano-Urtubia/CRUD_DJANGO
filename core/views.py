from django.shortcuts import render
from core import models
from .models import Producto
# Create your views here.

def home(request):
    productos = Producto.objects.all()
    return render(request,"core/index.html",{'productos':productos})


    