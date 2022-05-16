from django.db import models
from django.contrib.auth.models import User
import datetime

class Laboratorio(models.Model): #tabla que contiene los laboratorios fabricantes de medicamentos
    idLab = models.AutoField(primary_key=True) #id del laboratorio, es un autoincremental clave primaria que se utiliza en la tabla medicamento
    nombreLab = models.CharField(max_length=25) #nombre del laboratorio, para detalle

    def __str__(self):
        return self.nombreLab

class Formato(models.Model): #esta tabla contiene el formato en el que viene el medicamento
    idFormato = models.AutoField(primary_key=True) #id autoincremental, clave primaria que se utiliza en la tabla medicamento
    nombreFormato = models.CharField(max_length=25)#nombre del formato, por ejemplo cápsula, jarabe, gotas, etc
    
    def __str__(self):
        return self.nombreFormato

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombreCat = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombreCat

    
class Medicamento(models.Model): #esta tabla guarda la información relacionada al medicamento
    codigo = models.AutoField(primary_key=True) #codigo asignado de acuerdo a control interno, es clave primaria
    nombreMed = models.CharField(max_length=25) #es el nombre comercial del medicamento
    principio = models.CharField(max_length=40) #el principio activo del medicamento
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT, default=0)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.RESTRICT) #laboratorio que lo fabrica, se obtiene de la tabla Laboratorio
    formato = models.ForeignKey(Formato, on_delete=models.RESTRICT) #el formato de venta del medicamento, se obtiene de la tabla Formato
    stock = models.IntegerField() #la cantidad que hay en existencias del medicamento
    vencimiento = models.DateField() #la fecha de vencimiento indicada por el fabricante
    reservado = models.IntegerField(default=0) #en esta variable se guarda la cantidad de medicamentos reservados

    def __str__(self):
        return self.nombreMed

class Paciente(models.Model):
    rutPaciente = models.CharField(primary_key=True, max_length=10)
    nombresPac = models.CharField(max_length=40)
    apellidosPac = models.CharField(max_length=40)
    telefonoPac = models.IntegerField() #el telefono del paciente para enviar whatsapp
    correoPac = models.CharField(max_length=60) #el correo del paciente para enviar mensaje

    def __str__(self):
        return self.nombresPac +(" ")+ self.apellidosPac

class Receta(models.Model): #Esta tabla contiene la receta que es entregada por el médico para uso interno en farmacia
    idReceta = models.AutoField(primary_key=True) #id autoincremental que es clave primaria, para control interno
    medicamento = models.ManyToManyField(Medicamento)
    fechaReceta = models.DateTimeField(auto_now_add=True) #se añade automaticamente la fecha en que se ingreso la receta
    rutPaciente = models.ForeignKey(Paciente, on_delete=models.RESTRICT) #es el rut del paciente al cual se le hace la receta
    rutMed = models.ForeignKey(User, on_delete=models.RESTRICT) #el rut del médico que receta la orden, se obtiene de la tabla Usuario
    observacion = models.CharField(max_length=200) #una observación adicional del médico en caso de ser necesaria, o un detalle de la toma de medicamentos
    rutReceptor = models.CharField(editable=False, default=0, max_length=10)
    entregada = models.BooleanField()

    def __str__(self):
        idShow = str(self.fechaReceta) + (" ") + str(self.rutPaciente)
        return idShow




