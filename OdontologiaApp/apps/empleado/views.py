from django.shortcuts import render,redirect
from .models import Empleado
from .forms import EmpleadoForm
# Create your views here.

#Nuevo empleado
def nuevoEmpleado(request):  
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)       
        if form.is_valid():           
            form.save()                       
        return redirect('lista_empleado')   
    else:
        form = EmpleadoForm()
    return render(request, 'empleado/nuevoempleado.html', {'form': form})

#Eliminar empleado
def eliminarEmpleado(request, rut):
    empleado = Empleado.objects.get(rut = rut)
    if request.method == 'POST':
        empleado.delete()
        return redirect('lista_empleado')
    return render(request, 'empleado/eliminarempleado.html', {'empleado': empleado})

#Modificar un empleado
def modificarEmpleado(request, rut):
    empleado = Empleado.objects.get(rut = rut)
    if request.method == 'GET':
        form = EmpleadoForm(instance=empleado)
    else:
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('lista_empleado')
    return render(request, 'empleado/nuevoempleado.html', {'form': form})

#listar empleados
def listarEmpleados(request):
    #Carga nuevo empleado
    nuevoEmpleado(request)
    #lista a todos los empleados
    empleado = Empleado.objects.all()
    contexto = {'empleados':empleado, 'form': EmpleadoForm()}
    return render (request, 'empleado/listaempleado.html', contexto)