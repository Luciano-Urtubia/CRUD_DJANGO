from django.shortcuts import render, redirect, reverse
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def product_list(request):
    productos = Producto.objects.all()
    return render(request,"core/product-list.html",{'productos':productos})

def product_new(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            idProducto = form.cleaned_data.get("idProducto")
            descripcion = form.cleaned_data.get("descripcion")
            precio = form.cleaned_data.get("precio")
            stock = form.cleaned_data.get("stock")
            imagen = form.cleaned_data.get("imagen")
            marca = form.cleaned_data.get("marca")
            obj = Producto.objects.create(
                idProducto = idProducto,
                descripcion = descripcion,
                precio = precio,
                stock = stock,
                imagen = imagen,
                marca = marca
            )
            obj.save()
            return redirect(reverse('product-new') + "?OK")
            #return redirect(to ='product-list')
        else:
            return redirect(reverse('product-new') + "?FAIL")
    else:
        form = ProductoForm
    return render(request,"core/product-new.html",{'form':form})