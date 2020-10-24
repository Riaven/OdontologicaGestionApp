from django.urls import path
from .views import nuevoEmpleado

urlpatterns = [
    path('nuevo/', nuevoEmpleado, name="nuevo_empleado"),
]