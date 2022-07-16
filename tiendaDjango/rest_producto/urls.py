from  django.urls import path
from .views import detalle_producto, lista_producto

urlpatterns = [
    path('lista-producto',lista_producto,name="lista_producto"),
    path('detalle-producto/<id>', detalle_producto, name="detalle_producto")
]