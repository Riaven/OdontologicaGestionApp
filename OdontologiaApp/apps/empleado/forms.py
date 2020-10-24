from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):

    class Meta():
        model = Empleado
        fields = [
           'rut',
           'nombre',
           'apellido',
           'direccion',
           'telefono',
           'correo', 
        ]
        labels = {
           'rut' : 'RUN',
           'nombre' : 'Nombre' ,
           'apellido' : 'Apellido',
           'direccion' : 'Dirección',
           'telefono' : 'Teléfono',
           'correo' : 'Correo electrónico', 
        }

        widgets = {
           'rut' : forms.TextInput(attrs={'class' : 'input-field'}),
           'nombre' : forms.TextInput(attrs={'class' : 'input-field'}),
           'apellido' : forms.TextInput(attrs={'class' : 'input-field'}),
           'direccion' : forms.Textarea(),
           'telefono' : forms.TextInput(attrs={'class' : 'input-field'}),
           'correo' : forms.TextInput(attrs={'class' : 'input-field'}), 
        }