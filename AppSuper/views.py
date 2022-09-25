from django.shortcuts import render
from django.http import HttpResponse
from AppSuper.models import *
from AppSuper.forms import *
# Create your views here.

def inicio(request):
    return render(request, "AppSuper/inicio.html")
    


def cajero(request):

    cajero= Cajero(nombre = "F", apellido= "Gonzales", camada= 122553)

    cajero.save()

    return render(request, "AppSuper/cajero.html")


def cliente(request):
    
    cliente1= Cliente(nombre = "F", camada = 1223)

    cliente1.save()

    return render(request, "AppSuper/cliente.html")
    

def producto(request):

    producto= Producto(nombre = "F", camada= 454, precio = 1223)

    producto.save()
    return render(request, "AppSuper/producto.html")

def formulario(request):

    if request.method=="POST":

            formulario1 = FormularioCliente(request.POST)

            if formulario1.is_valid(): #Comprobar que no haya errores

                info= formulario1.cleaned_data # Para que no sea necesario escribir nombre=request.POST["curso"],

                clienteF = Cliente(nombre=info["nombre"], camada=info["camada"])

                clienteF.save()

                return render(request, "AppSuper/inicio.html")
    else:

            formulario1 = FormularioCliente() #mostrar el formulario vacio

    return render(request, "AppSuper/formulario.html", {"form1": formulario1})

def busquedaCamada(request):


    return render(request, "AppSuper/inicio.html")

def buscar(request):

    if request.GET["camada"]:

        busqueda = request.GET["camada"]
        clientes = Cliente.objects.filter(camada__iexact=busqueda)
        
        return render(request, "AppSuper/inicio.html", {"clientes" : clientes, "busqueda":busqueda})
    
    else:
        mensaje = "No enviaste datos."

    return HttpResponse(mensaje)

#cajeroformulario
def formulario2(request):

    if request.method=="POST":

            formulario2 = FormularioCajero(request.POST)

            if formulario2.is_valid(): #Comprobar que no haya errores

                info= formulario2.cleaned_data # Para que no sea necesario escribir nombre=request.POST["curso"],

                cajero = Cajero(nombre=info["nombre"], apellido=info["apellido"] ,camada=info["camada"])

                cajero.save()

                return render(request, "AppSuper/inicio.html")
    else:

            formu2 = FormularioCajero() #mostrar el formulario vacio

    return render(request, "AppSuper/cajeroFormulario.html", {"form2": formu2})

def busquedaCajero(request):


    return render(request, "AppSuper/busquedaCajero.html")

def buscar1(request):

    if request.GET["camada"]:

        busqueda1 = request.GET["camada"]
        cajeros = Cajero.objects.filter(camada__iexact=busqueda1)
        return render(request, "AppSuper/buscar1.html", {"cajeros": cajeros, "busqueda1":busqueda1})
    
    else:
        mensaje = "No enviaste datos."

    return HttpResponse(mensaje)


#productoformulario
def formulario3(request):

    if request.method=="POST":

            formulario3 = FormularioProducto(request.POST)

            if formulario3.is_valid(): #Comprobar que no haya errores

                info= formulario3.cleaned_data # Para que no sea necesario escribir nombre=request.POST["curso"],

                cajero = Producto(nombre=info["nombre"], camada=info["camada"], precio=info["precio"])

                cajero.save()

                return render(request, "AppSuper/inicio.html")
    else:

            formu3 = FormularioProducto() #mostrar el formulario vacio

    return render(request, "AppSuper/cajeroProducto.html", {"form3": formu3})

def busquedaProducto(request):


    return render(request, "AppSuper/busquedaProducto.html")

def buscar2(request):

    if request.GET["camada"]:

        busqueda2 = request.GET["camada"]
        productos = Producto.objects.filter(camada__iexact=busqueda2)
        return render(request, "AppSuper/buscar2.html", {"productos": productos, "busqueda2":busqueda2})
    
    else:
        mensaje = "No enviaste datos."

    return HttpResponse(mensaje)