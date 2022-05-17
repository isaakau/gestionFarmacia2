from django.db import models
from django.contrib.auth.models import User

class Laboratorio(models.Model): #tabla que contiene los laboratorios fabricantes de medicamentos
    idLab = models.AutoField(primary_key=True, verbose_name="Id del laboratorio (uso interno)") #id del laboratorio, es un autoincremental clave primaria que se utiliza en la tabla medicamento
    nombreLab = models.CharField(max_length=25, verbose_name="Nombre del Laboratorio") #nombre del laboratorio, para detalle

    def __str__(self):
        return self.nombreLab

class Formato(models.Model): #esta tabla contiene el formato en el que viene el medicamento
    idFormato = models.AutoField(primary_key=True, verbose_name="Id del Formato (uso interno)") #id autoincremental, clave primaria que se utiliza en la tabla medicamento
    nombreFormato = models.CharField(max_length=25, verbose_name="Formato del Medicamento")#nombre del formato, por ejemplo cápsula, jarabe, gotas, etc
    
    def __str__(self):
        return self.nombreFormato

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True, verbose_name="ID de la Categoría (uso interno)")
    nombreCat = models.CharField(max_length=40, verbose_name="Nombre de la Categoría")
    descripcion = models.CharField(max_length=200, verbose_name="Descripción de la Categoría")

    def __str__(self):
        return self.nombreCat

    
class Medicamento(models.Model): #esta tabla guarda la información relacionada al medicamento
    codigo = models.AutoField(primary_key=True, verbose_name="Código del Medicamento") #codigo asignado de acuerdo a control interno, es clave primaria
    nombreMed = models.CharField(max_length=25, verbose_name="Nombre del Medicamento") #es el nombre comercial del medicamento
    principio = models.CharField(max_length=40, verbose_name="Principio Activo") #el principio activo del medicamento
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT, default=0)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.RESTRICT) #laboratorio que lo fabrica, se obtiene de la tabla Laboratorio
    formato = models.ForeignKey(Formato, on_delete=models.RESTRICT) #el formato de venta del medicamento, se obtiene de la tabla Formato
    stock = models.IntegerField(verbose_name="Stock del Medicamento") #la cantidad que hay en existencias del medicamento
    vencimiento = models.DateField(verbose_name="Fecha de Vencimiento") #la fecha de vencimiento indicada por el fabricante

    def __str__(self):
        return str(self.codigo)

class Paciente(models.Model):
    rutPaciente = models.CharField(primary_key=True, max_length=10, verbose_name="Rut del Paciente")
    nombresPac = models.CharField(max_length=40, verbose_name="Nombres del Paciente")
    apellidosPac = models.CharField(max_length=40, verbose_name="Apellidos del Paciente")
    telefonoPac = models.IntegerField(verbose_name="Celular del Paciente") #el telefono del paciente para enviar whatsapp
    correoPac = models.CharField(max_length=60, verbose_name="Correo electrónico del Paciente") #el correo del paciente para enviar mensaje

    def __str__(self):
        return self.nombresPac +(" ")+ self.apellidosPac

class Receta(models.Model): #Esta tabla contiene la receta que es entregada por el médico para uso interno en farmacia
    idReceta = models.AutoField(primary_key=True, verbose_name="Id de la Receta (uso interno)") #id autoincremental que es clave primaria, para control interno
    #medicamento = models.ManyToManyField(Medicamento) #este se sacaría porque iría en la entidad de abajo
    fechaReceta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Emisión") #se añade automaticamente la fecha en que se ingreso la receta
    rutPaciente = models.ForeignKey(Paciente, on_delete=models.RESTRICT) #es el rut del paciente al cual se le hace la receta
    rutMed = models.ForeignKey(User, on_delete=models.RESTRICT) #el rut del médico que receta la orden, se obtiene de la tabla Usuario
    observacion = models.CharField(max_length=200, verbose_name="Observación del Médico") #una observación adicional del médico en caso de ser necesaria, o un detalle de la toma de medicamentos
    rutReceptor = models.CharField(editable=False, default=0, max_length=10, verbose_name="Rut del que Retira")
    entregada = models.BooleanField(verbose_name="Receta Entregada")

    def __str__(self):
        return str(self.idReceta)

class DetalleReceta(models.Model):
    idDetalle = models.AutoField(primary_key=True)
    idReceta = models.ForeignKey(Receta, on_delete=models.RESTRICT)
    codmed = models.ForeignKey(Medicamento, on_delete=models.RESTRICT)
    cantidad = models.IntegerField(verbose_name="Cantidad del Medicamento") #cantidad del medicamento ingresado en la receta

    def __str__(self):
        detalle = "receta_n" + str(self.idReceta)+"medicamento_"+str(self.codmed)
        return detalle


class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True)
    idDetalle = models.ForeignKey(DetalleReceta, on_delete=models.RESTRICT)
    codMed = models.ForeignKey(Medicamento, on_delete=models.RESTRICT)
    rutPaciente = models.ForeignKey(Paciente, on_delete=models.RESTRICT)
    cantidadReservada = models.IntegerField()

    def __str__(self):
        return self.idReserva


