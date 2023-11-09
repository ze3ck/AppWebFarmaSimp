from tkinter import Label
from typing import ChainMap
from django.db import models

# Create your models here.
class Medicamento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=40,null=True,verbose_name="Nombre del medicamento")
    descripcionMedicamento=models.CharField(max_length=40,null=True,verbose_name="Descripcion")
    fabricanteMedicamento=models.CharField(max_length=40,null=True,verbose_name="Fabricante")
    contenidoMedicamento=models.CharField(max_length=40,null=True,verbose_name="Contenido")
    cantidad = models.IntegerField(verbose_name='Cantidad',null=True)
    gramaje = models.IntegerField(verbose_name='Gramaje',null=True)
    precio = models.IntegerField(verbose_name='Precio',null=True)
    imagenPublicacion=models.ImageField(upload_to="fotopublicaciones",null=True)
    caducado=models.CharField(max_length=2,null=True,verbose_name="caducar")
    


    def __str__(self) :
        return self.nombre

class Consulta(models.Model):
    codigo2 = models.AutoField(primary_key=True)
    rut=models.CharField(max_length=10,null=True,verbose_name="Rut del paciente")
    nombrePersona=models.CharField(max_length=40,null=True,verbose_name="Nombre del paciente")
    Sintomas=models.TextField(max_length=300,null=True,verbose_name="Sintomas")
    diagnostico=models.TextField(max_length=300,null=True,verbose_name="Diagnostico")
    medicamentoRecetado=models.ForeignKey(Medicamento,on_delete=models.CASCADE,verbose_name="Medicamento")
    

    def __str__(self) :
        return self.nombrePersona

class Retiro(models.Model):
    codigoRetiro = models.AutoField(primary_key=True)
    rut=models.CharField(max_length=10,null=True,verbose_name="Rut de la persona que retira")
    nombrePersona2=models.CharField(max_length=40,null=True,verbose_name="Nombre de la persona que retira")
    apellidoPersona=models.CharField(max_length=40,null=True,verbose_name="Apellido de la persona que retira")
    cantidad=models.IntegerField(verbose_name='Cantidad',null=True)
    medicamento=models.ForeignKey(Medicamento,on_delete=models.CASCADE)

    def __str__(self) :
        return self.rut
    



