from django.db import models

# Create your models here.
class Empleado (models.Model):
    
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=60)
    direccion = models.TextField()
    telefono = models.CharField(max_length=12)
    correo = models.EmailField()

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)