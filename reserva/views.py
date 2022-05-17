from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import MedicamentoForm
# Aquí es donde declaramos nuestras vistas personalizadas, a partir de los html que tenemos en la carpeta templates
#en el codigo de abajo solo se pone reserva porque la función busca automáticamente la carpeta templates
def home(request):
    return render(request, 'reserva/home.html') 
#lo que hicimos fue definir como home, el archivo html que se llama home
#esto quiere decir que cuando la url de la pagina no tenga nada después del /, nos redirecciona a esta pagina home
def login(request):
    return render(request, 'reserva/login.html') 

def gestion_medicamentos(request):
    meds = Medicamento.objects.all()
    context = {'meds':meds}
    return render(request, 'reserva/VerMedicamentos.html', context)

def crear_medicamento(request):

    data = {
        'form': MedicamentoForm()
    }
    
    if request.method == 'POST':
        formulario = MedicamentoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado exitosamente"
        else:
            data["form"] = Medicamento
    
    return render(request, 'reserva/agregarMedicamentos.html', data)
    

def modificar_medicamento(request, codigo):
    medicamento = get_object_or_404(Medicamento, codigo=codigo)
    
    data = {
        'form': MedicamentoForm(instance=medicamento)
    }

    if request.method == 'POST':
        formulario = MedicamentoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Modificado exitosamente"
            return redirect(to="gestion_medicamentos")
        data["form"] = formulario

    return render(request, 'reserva/modificarMedicamento.html')

def receta(request):
    meds = Medicamento.objects.all()
    context = {'meds':meds}
    return render(request, 'reserva/receta.html', context) 

def crear_receta(request):
    # if request.user.is_authenticated:
    #     # medico = request.user.User
    #     receta, created = Receta.objects.get_or_create(entregada=False)
    #     medicamentos = receta.receta_set.all()
    # else:
    #     medicamentos = []
    context = {}
    return render(request, 'reserva/crear_receta.html', context) 

def finalizar_receta(request):
    context = {}
    return render(request, 'reserva/finalizar_receta.html', context) 