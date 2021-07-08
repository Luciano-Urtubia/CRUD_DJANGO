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


def product_update(request, idProducto):
    producto = Producto.objects.get(idProducto = idProducto)
    form = ProductoForm( instance = producto )
    #return render (request, "core/product-update.html",{'form':form})

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance = producto)
        if form.is_valid():
            form.save()
            return redirect(reverse('product-list')+ "?OK")
        else:
            return redirect(reverse('product-update')+ idProducto)

    return render(request,"core/product-update.html",{'form':form})


def product_delete(request,idProducto):
    producto = Producto.objects.get(idProducto = idProducto)
    producto.delete()
    return redirect(to='product-list')   


#----------------------------------------------------------------------------------------------------------    


def pc_list(request):
    productosPc = ProductoPc.objects.all()
    return render(request,"core/product-list.html",{'productosPc':productosPc})

def product_newPc(request):
    if request.method == 'POST':
        form = ProductoPcForm(request.POST, request.FILES)
        if form.is_valid():
            idProductoPc = form.cleaned_data.get("idProductoPC")
            descripcionPc = form.cleaned_data.get("descripcion")
            precioPc = form.cleaned_data.get("precio")
            stockPc = form.cleaned_data.get("stock")
            imagenPc = form.cleaned_data.get("imagen")
            marcaPc = form.cleaned_data.get("marca")
            obj = ProductoPc.objects.create(
                idProductoPC = idProductoPC,
                descripcionPc = descripcionPc,
                precioPc = precioPc,
                stockPc = stockPc,
                imagenPc = imagenPc,
                marcaPc = marcaPc,
            )
            obj.save()
            return redirect(reverse('product-new') + "?OK")
            #return redirect(to ='product-list')
        else:
            return redirect(reverse('product-new') + "?FAIL")
    else:
        form = ProductoPcForm
    return render(request,"core/product-new.html",{'form':form})





def product_updatePc(request, idProducto):
    productoPc = ProductoPc.objects.get(idProductoPc = idProductoPc)
    form = ProductoPcForm( instance = productoPc )
    #return render (request, "core/product-update.html",{'form':form})

    if request.method == 'POST':
        form = ProductoPcForm(request.POST, request.FILES, instance = productoPc)
        if form.is_valid():
            form.save()
            return redirect(reverse('product-list')+ "?OK")
        else:
            return redirect(reverse('product-update')+ idProductoPc)

    return render(request,"core/product-update.html",{'form':form})    




    


def product_deletePc(request,idProductoPC):
    productoPc = ProductoPc.objects.get(idProductoPc = idProductoPc)
    productoPc.delete()
    return redirect(to='product-list') 