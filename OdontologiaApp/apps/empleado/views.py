from django.shortcuts import render
from .models import Empleado
from .forms import EmpleadoForm
# Create your views here.


def nuevoEmpleado(request):  
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)       
        if form.is_valid():           
            form.save()                       
        #return redirect('listar_fichas')   
    else:
        form = EmpleadoForm()
    return render(request, 'empleado/nuevoempleado.html', {'form': form})