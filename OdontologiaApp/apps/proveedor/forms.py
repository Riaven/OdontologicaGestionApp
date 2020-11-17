from django import forms
from .models import Proveedor

class ProveedorForm (forms.ModelForm):
    class Meta():
        model = Proveedor
        fields = [
           'id_proveedor',
           'nombre',
           'telefono',
           'direccion',
           'rubro',
        ]
        labels = {
           'id_proveedor' : 'Id proveedor',
           'nombre' : 'Nombre' ,
           'telefono' : 'Teléfono',
           'direccion' : 'Dirección',
           'rubro' : 'Rubro', 
        }

        widgets = {
           'id_proveedor' : forms.TextInput(attrs={'class' : 'input-field'}),
           'nombre' : forms.TextInput(attrs={'class' : 'input-field'}),
           'telefono' : forms.TextInput(attrs={'class' : 'input-field'}),
           'direccion' : forms.Textarea(),
           'rubro' : forms.Select(attrs={'class' : 'select'}),
        } 
        



