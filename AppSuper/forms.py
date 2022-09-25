from django import forms


class FormularioCajero(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField(max_length=60)
    camada = forms.IntegerField()

class FormularioCliente(forms.Form):

    nombre = forms.CharField()
    camada = forms.IntegerField()

class FormularioProducto(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()
    precio = forms.IntegerField()
