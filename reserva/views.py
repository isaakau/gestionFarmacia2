from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required

# Aquí es donde declaramos nuestras vistas personalizadas, a partir de los html que tenemos en la carpeta templates
#en el codigo de abajo solo se pone reserva porque la función busca automáticamente la carpeta templates
def home(request):
    return render(request, 'reserva/home.html') 
#lo que hicimos fue definir como home, el archivo html que se llama home
#esto quiere decir que cuando la url de la pagina no tenga nada después del /, nos redirecciona a esta pagina home

@permission_required('reserva.view_medicamento')
def gestion_medicamentos(request):
    #este metodo abre el mantenedor creado en ese html 
    meds = Medicamento.objects.all() #aqui se guardan todos los objetos de la tabla Medicamento en la BD
    context = {'meds':meds} #este meds es el que se usa en el for del html para listar cada elemento
    return render(request, 'reserva/VerMedicamentos.html', context)

@permission_required('reserva.add_medicamento')
def crear_medicamento(request):
    #este metodo sirve para crear un medicamento nuevo
    data = {
        'form': MedicamentoForm()
    }
    #aca verifica que si el metodo es post, revisa que el formulario este valido y lo guarda, enviando un mensaje que se refleja abajo de la pantalla
    if request.method == 'POST':
        form = MedicamentoForm(data=request.POST)
        if form.is_valid():
            form.save()
            data["mensaje"] = "Guardado exitosamente"
        else:
            data["form"] = form
    
    return render(request, 'reserva/agregarMedicamentos.html', data)
    
@permission_required('reserva.change_medicamento')
def modificar_medicamento(request, codigo):
    #este metodo es el que modifica un medicamento,
    meds = Medicamento.objects.get(codigo=codigo)
    antiguoStock = meds.stock #este valor lo tomo aqui para la logica que se usa mas abajo
    data = {
        'form': MedicamentoForm(instance=meds)
    } 
    
    if request.method == 'POST':
        form = MedicamentoForm(data=request.POST, instance=meds)
        if form.is_valid():
            print("válido")
            #aqui tiene que ir la funcion que valide el stock y mande las alertas.
            nuevoStock = request.POST["stock"] #aca capturo el otro stock
            print(nuevoStock)
            print(antiguoStock)
            #esto es para probar que detecta los cambios de stock
            if int(nuevoStock)>int(antiguoStock): #aca se evalua si el stock nuevo es mayor respecto al antiguo, osea si se repuso stock de un medicamento
                #esta es la logica basa que se debe usar para lo de las reservas
                print("Se aumentó el stock")
            else:
                print("Se disminuyó el stock")
            #     reservados = 0
            #     for i in Reserva(idReserva):
            #         if Reserva.objects.get(codMed=codigo):
            #             print(Reserva(idReserva))
            #             reservados = reservados + Reserva(cantidadReservada)
            #             #aca faltaría capturar en una lista los telefonos y mails de las personas que tienen reserva, se puede hacer aqui o en otro metodo
            #     print(reservados)
            #     #una vez terminado ese for, debería comparar si el stock nuevo alcanza a suplir las reservas, si pasa dentro del if, se mandan los mensajes
            #     #y se borran las filas en Reserva
            form.save()
            return redirect(to="gestion_medicamentos")
        else:
            data["form"] = form

    return render(request, 'reserva/modificarMedicamento.html', data)
@permission_required('reserva.view_receta')
def listar_recetas(request):
    recetas = Receta.objects.all()
    context = {'recetas':recetas}
    return render(request, 'reserva/listarRecetas.html', context)

def receta(request):
    meds = Medicamento.objects.all()
    context = {'meds':meds}
    return render(request, 'reserva/receta.html', context) 

@permission_required('reserva.add_receta')
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
    if request.user.is_authenticated:
        receta, created = Receta.objects.get_or_create(entregada=False)
        listaMeds = receta.detallereceta_set.all()
    else:
        listaMeds = []
        receta = {'get_meds_total':0}
    context = {'listaMeds':listaMeds}
    return render(request, 'reserva/finalizar_receta.html', context) 
