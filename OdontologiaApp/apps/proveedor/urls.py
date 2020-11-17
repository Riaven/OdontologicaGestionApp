from django.urls import path, re_path
from .views import nuevoProveedor, modificarProveedor, listarProveedor, eliminarProveedor

urlpatterns = [
    path('nuevo/', nuevoProveedor, name="nuevo_proveedor"),
    path('', listarProveedor, name="lista_proveedor"),
    path('eliminar/(?P<id_proveedor>\d+)/', eliminarProveedor, name="elimina_proveedor"),
    path('modificar/(?P<id_proveedor>\d+)/', modificarProveedor, name="modificar_proveedor"),
]

