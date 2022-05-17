from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Laboratorio)
admin.site.register(Formato)
admin.site.register(Categoria)
admin.site.register(Medicamento)
admin.site.register(Paciente)
admin.site.register(Receta)
admin.site.register(DetalleReceta)
admin.site.register(Reserva)