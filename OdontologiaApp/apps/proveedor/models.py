from django.db import models

class Rubro (models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.nombre)

# Create your models here.
class Proveedor (models.Model):
    id_proveedor = models.CharField(max_length = 15, primary_key = True)
    nombre = models.CharField(max_length = 40)
    telefono = models.CharField(max_length= 12)
    direccion = models.CharField(max_length=80)
    #rubro = models.CharField(max_length = 50)
    rubro = models.ForeignKey(Rubro, on_delete = models.CASCADE)

    def __str__(self):
        return "{}".format(self.nombre)