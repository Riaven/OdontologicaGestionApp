from django.shortcuts import render, redirect
from .models import Proveedor
from .forms import ProveedorForm

# Create your views here.
#nuevo proveedor
def nuevoProveedor(request):  
    if request.method == 'POST':
        form = ProveedorForm(request.POST)       
        if form.is_valid():           
            form.save()                       
        return redirect('lista_proveedor')   
    else:
        form = ProveedorForm()
    return render(request, 'proveedor/nuevoproveedor.html', {'form': form})

#Eliminar proveedor
def eliminarProveedor(request, id_proveedor):
    proveedor = Proveedor.objects.get(id_proveedor = id_proveedor)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('lista_proveedor')
    return render(request, 'proveedor/eliminarproveedor.html', {'proveedor': proveedor})
    
# Modificar un proveedor
def modificarProveedor(request, id_proveedor):
    proveedor = Proveedor.objects.get(id_proveedor = id_proveedor)
    if request.method == 'GET':
        form = ProveedorForm(instance = proveedor)
    else:
        form = ProveedorForm(request.POST, instance = proveedor)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedor')
    return render(request, 'proveedor/nuevoproveedor.html', {'form': form})

#Listar proveedores#
def listarProveedor(request):
    nuevoProveedor(request) #cargamos para que pueda agregar un nuevo registro desde la lista de proveedores
    proveedor = Proveedor.objects.all()
    #pasamos un diccionario para listar y otro para cargar el formulario
    contexto = {'proveedores': proveedor, 'form':ProveedorForm()}
    return render (request, 'proveedor/listaproveedor.html', contexto)