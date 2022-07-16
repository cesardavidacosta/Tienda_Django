from django.shortcuts import render, redirect

from core.forms import Productoform

from .models import Producto

#class Productos:
 #   def __init__(self, nombre,valor) :
 #       self.nombre = nombre
 #       self.valor = valor
 #       super().__init__()

# Create your views here.
#def home(request):

 #   vinilo = Productos("Cd de Aerosmith", 19900)

 #   lista = [" DEADPOOL"," WOLVERINE","HULK"]
 #   contexto = {"nombre":"Cesar David","Heroes":lista,"vinilo":vinilo}

 #   return render(request,'core/home.html',contexto)

def home(request):
    productos = Producto.objects.all()
    contexto = {
        'productos':productos
    }
    return render(request,'core/home.html',contexto)

def form_producto(request):
    
    contexto = {
        'form': Productoform()
    }
    if request.method == 'POST':
        formulario = Productoform(request.POST)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje']= "el producto se ha guardado correctamente"
    return render(request,'core/form_producto.html', contexto) 

def form_mod_producto(request,id):
    producto = Producto.objects.get(idProducto = id)
    contexto ={
        'form' : Productoform (instance=producto)
    }
    if request.method == 'POST':
        formulario = Productoform(data=request.POST,instance=producto)
        if  formulario.is_valid:
            formulario.save()
            contexto['mensaje']= "se ha modificado correctamente"

    return render(request,'core/form_mod_producto.html', contexto)

def form_del_producto(request,id):
    producto = Producto.objects.get(idProducto = id)
    producto.delete()
    return redirect(to="home")