from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
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
        form = MedicamentoForm(data=request.POST)
        if form.is_valid():
            form.save()
            data["mensaje"] = "Guardado exitosamente"
        else:
            data["form"] = form
    
    return render(request, 'reserva/agregarMedicamentos.html', data)
    

def modificar_medicamento(request, codigo):
    meds = Medicamento.objects.get(codigo=codigo)
    antiguoStock = meds.stock
    data = {
        'form': MedicamentoForm(instance=meds)
    } 
    
    if request.method == 'POST':
        form = MedicamentoForm(data=request.POST, instance=meds)
        if form.is_valid():
            print("válido")
            #aqui tiene que ir la funcion que valide el stock y mande las alertas.
            nuevoStock = request.POST["stock"]
            print(nuevoStock)
            print(antiguoStock)
            #esto es para probar que detecta los cambios de stock
            if int(nuevoStock)>int(antiguoStock):
                print("Se aumentó el stock")
            else:
                print("Se disminuyó el stock")
            #     reservados = 0
            #     for i in Reserva(idReserva):
            #         if Reserva.objects.get(codMed=codigo):
            #             print(Reserva(idReserva))
            #             reservados = reservados + Reserva(cantidadReservada)
            #             #aca faltaría capturar en una lista los telefonos y mails de las personas que tienen reserva
            #     print(reservados)
            #     #una vez terminado ese for, debería comparar si el stock nuevo alcanza a suplir las reservas, si pasa dentro del if, se mandan los mensajes
            #     #y se borran las filas en Reserva
            form.save()
            return redirect(to="gestion_medicamentos")
        else:
            data["form"] = form

    return render(request, 'reserva/modificarMedicamento.html', data)

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

