from itertools import product
from django import forms
from django.forms import ModelForm
from .models import Producto

class Productoform(ModelForm):
    class Meta:
        model= Producto
        fields =['idProducto','nombreProducto','valorProducto','categoria' ]
