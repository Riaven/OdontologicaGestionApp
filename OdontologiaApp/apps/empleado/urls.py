from django.urls import path, re_path
from .views import nuevoEmpleado, listarEmpleados, modificarEmpleado, eliminarEmpleado

urlpatterns = [
    path('nuevo/', nuevoEmpleado, name="nuevo_empleado"),
    path('', listarEmpleados, name="lista_empleado"),
    path('eliminar/(?P<rut>\d+)/', eliminarEmpleado, name="elimina_empleado"),
    path('modificar/(?P<rut>\d+)/', modificarEmpleado, name="modificar_empleado"),
]
