from django.shortcuts import render
from .models import *
# Aquí es donde declaramos nuestras vistas personalizadas, a partir de los html que tenemos en la carpeta templates
#en el codigo de abajo solo se pone reserva porque la función busca automáticamente la carpeta templates
def home(request):
    return render(request, 'reserva/home.html') 
#lo que hicimos fue definir como home, el archivo html que se llama home
#esto quiere decir que cuando la url de la pagina no tenga nada después del /, nos redirecciona a esta pagina home
def login(request):
    return render(request, 'reserva/login.html') 

def receta(request):
    meds = Medicamento.objects.all()
    context = {'meds':meds}
    return render(request, 'reserva/receta.html', context) 

def crear_receta(request):
    if request.user.is_authenticated:
        receta, created = Receta.objects.get_or_create(entregada=False)
        listaMeds = receta.detallereceta_set.all()
    else:
        listaMeds = []
        receta = {'get_meds_total':0}
    context = {'listaMeds':listaMeds}
    return render(request, 'reserva/crear_receta.html', context) 

def finalizar_receta(request):
    context = {}
    return render(request, 'reserva/finalizar_receta.html', context) 