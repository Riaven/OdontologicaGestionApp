from django.urls import path
from .views import nuevoEmpleado, listarEmpleados, modificarEmpleado, eliminarEmpleado

urlpatterns = [
    path('nuevo/', nuevoEmpleado, name="nuevo_empleado"),
    path('lista/', listarEmpleados, name="lista_empleado"),
    path('eliminar/(?P<rut>\d+)/', eliminarEmpleado, name="elimina_empleado"),
    path('modificar/(?P<rut>\d+)/', modificarEmpleado, name="modificar_empleado"),
]

"""
url(r'^$', listarProfesionales, name='profesionales'),
    #url(r'^nuevo$', nuevoProfesional, name="nuevoprofesional"), 
    url(r'^eliminar/(?P<id>\d+)/$', eliminarProfesional, name='eliminar_profesional'),
    url(r'^modificar/(?P<id>\d+)/$', modificarProfesional, name='modificar_profesional'),
"""