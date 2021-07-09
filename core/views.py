from django.shortcuts import render, redirect, reverse
from .models import Producto 
from .models import ProductoPC
from .models import Productocelular
from .models import roductoRi
from .forms import ProductoForm
from .forms2 import ProductoPcForm 





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

def lista2__(request):
    productosPc = ProductoPC.objects.all()
    return render(request,"core/lista_2.html",{'productosPc':productosPc})

def lista3__(request):
    productoscelular = Productocelular.objects.all()
    return render(request,"core/lista_3.html",{'productoscelular':productoscelular})    


def lista4__(request):
    productosRi = roductoRi.objects.all()
    return render(request,"core/lista_4.html",{'productosRi':productosRi})        

 #-------------------------------------------------------------------------------------------------------------  



def listaf2__(request): 
    listaf2_productoPc = ProductoPcForm
    return render(request,"core/listaf2.html",)

