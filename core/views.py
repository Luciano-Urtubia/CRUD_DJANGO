from django.shortcuts import render, redirect, reverse
from .models import Producto 
from .models import ProductoPC
from .forms import ProductoForm 
from .forms import ProductoPcForm 





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





 #---------------------------------------------------------------------------------  


def celular_list(request):
    productoscelular = Productocelular.objects.all()
    return render(request,"core/product-list.html",{'productoscelular':productoscelular})

def product_newcelular(request):
    if request.method == 'POST':
        form = ProductocelularForm(request.POST, request.FILES)
        if form.is_valid():
            idProductocelular = form.cleaned_data.get("idProductocelular")
            descripcioncelular = form.cleaned_data.get("descripcioncelular")
            preciocelular = form.cleaned_data.get("preciocelular")
            stockcelular = form.cleaned_data.get("stockcelular")
            imagencelular = form.cleaned_data.get("imagencelular")
            
            obj = Productocelular.objects.create(
                idProductocelular = idProductocelular,
                descripcioncelular = descripcioncelular,
                preciocelular = preciocelular,
                stockcelular = stockcelular,
                imagencelular = imagencelular,
               
            )
            obj.save()
            return redirect(reverse('product-new') + "?OK")
            #return redirect(to ='product-list')
        else:
            return redirect(reverse('product-new') + "?FAIL")
    else:
        form = ProductocelularForm
    return render(request,"core/product-new.html",{'form':form})





def product_updatecelular(request, idProductocelular):
    productocelular = Productocelular.objects.get(idProductocelular = idProductocelular)
    form = ProductocelularForm( instance = productocelular )
    #return render (request, "core/product-update.html",{'form':form})

    if request.method == 'POST':
        form = ProductocelularForm(request.POST, request.FILES, instance = productocelular)
        if form.is_valid():
            form.save()
            return redirect(reverse('product-list')+ "?OK")
        else:
            return redirect(reverse('product-update')+ idProductocelular)

    return render(request,"core/product-update.html",{'form':form})    




    


def product_deletecelular(request,idProductoPC):
    productocelular = Productocelular.objects.get(idProductocelular = idProductocelular)
    productocelular.delete()
    return redirect(to='product-list')  




#-------------------------------------------------------------------------------------------------------------------------------------    


def Ri_list(request):
    productosRi = ProductoRi.objects.all()
    return render(request,"core/product-list.html",{'productosRi':productosRi})

def product_newRi(request):
    if request.method == 'POST':
        form = ProductoRiForm(request.POST, request.FILES)
        if form.is_valid():
            idProductoRi = form.cleaned_data.get("idProductoRi")
            descripcionRi = form.cleaned_data.get("descripcionRi")
            precioRi = form.cleaned_data.get("precioRi")
            stockRi = form.cleaned_data.get("stockRi")
            imagenRi = form.cleaned_data.get("imagenRi")
            
            obj = ProductoRi.objects.create(
                idProductoRi = idProductoRi,
                descripcionRi = descripcionRi,
                precioRi = precioRi,
                stockRi = stockRi,
                imagenRi = imagenRi,
             
            )
            obj.save()
            return redirect(reverse('product-new') + "?OK")
            #return redirect(to ='product-list')
        else:
            return redirect(reverse('product-new') + "?FAIL")
    else:
        form = ProductoRiForm
    return render(request,"core/product-new.html",{'form':form})





def product_updateRi(request, idProductoRi):
    productoRi = ProductoRi.objects.get(idProductoRi = idProductoRi)
    form = ProductoRiForm( instance = productoRi )
    #return render (request, "core/product-update.html",{'form':form})

    if request.method == 'POST':
        form = ProductoRiForm(request.POST, request.FILES, instance = productoRi)
        if form.is_valid():
            form.save()
            return redirect(reverse('product-list')+ "?OK")
        else:
            return redirect(reverse('product-update')+ idProductoRi)

    return render(request,"core/product-update.html",{'form':form})    




    


def product_deleteRi(request,idProductoRi):
    productoRi = ProductoRi.objects.get(idProductoRi = idProductoRi)
    productoRi.delete()
    return redirect(to='product-list')  