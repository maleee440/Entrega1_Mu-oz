from django.urls import path
from AppSuper.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("cajero/", cajero, name="Cajero"),
    path("clientes/", cliente, name="Cliente"),
    path("productos/", producto, name="Productos"),
    path("formulario/", formulario, name="Formulario"),
    path("buscarCamada/", busquedaCamada, name="buscarCamada"),
    path("buscar/", buscar, name="resultadosBusqueda"),
    path("formulario2/", formulario2, name="Formulario2"),
    path("buscarCajero/", busquedaCajero, name="BuscarCajero"),
    path("buscar1/", buscar1, name="resultadosBusqueda2"),
    #formulario3
    path("formulario3/", formulario3, name="Formulario3"),
    path("buscarProducto/", busquedaProducto, name="BuscarProducto"),
    path("buscar2/", buscar2, name="resultadosBusqueda3"),
]