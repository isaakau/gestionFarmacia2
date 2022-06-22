from venv import create
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from .Carrito import *
import datetime
from django.db.models import Q

# Aquí es donde declaramos nuestras vistas personalizadas, a partir de los html que tenemos en la carpeta templates
#en el codigo de abajo solo se pone reserva porque la función busca automáticamente la carpeta templates
def home(request):
    return render(request, 'reserva/base.html') 
#lo que hicimos fue definir como home, el archivo html que se llama base
#esto quiere decir que cuando la url de la pagina no tenga nada después del /, nos redirecciona a esta pagina home

@permission_required('reserva.view_medicamento')
def gestion_medicamentos(request):
    #este metodo abre el mantenedor creado en ese html
    carrito = Carrito(request)
    queryset = request.GET.get("buscar")
    if queryset:
        meds = Medicamento.objects.filter(
            Q(nombreMed__icontains = queryset) |
            Q(principio__icontains = queryset)
        ).distinct()
    else:
        meds = Medicamento.objects.all() #aqui se guardan todos los objetos de la tabla Medicamento en la BD
    context = {'meds':meds} #este meds es el que se usa en el for del html para listar cada elemento

    return render(request, 'medicamentos/VerMedicamentos.html', context)

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
    
    return render(request, 'medicamentos/agregarMedicamentos.html', data)
    
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
                print("el stock aumento")
                authuser = request.user
                print(authuser)
                mail = authuser.email
                print(mail)
                send_email(mail)
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

    return render(request, 'medicamentos/modificarMedicamento.html', data)
@permission_required('reserva.view_receta')
def listar_recetas(request):
    queryset = request.GET.get("buscar")
    if queryset:
        recetas = Receta.objects.filter(
            Q(rutPaciente = queryset) 
        )
    else:
        recetas = Receta.objects.all()    
    context = {'recetas':recetas}
    return render(request, 'reserva/listarRecetas.html', context)

from django.views.decorators.csrf import csrf_exempt

#Para crear una nueva receta
def agregar_receta(request):
    # meds = Medicamento.objects.all()
    data = {
        'form': RecetaForm()
    }
    #aca verifica que si el metodo es post, revisa que el formulario este valido y lo guarda, enviando un mensaje que se refleja abajo de la pantalla
    if request.method == 'POST':
        form = RecetaForm(data=request.POST)
        if form.is_valid():
            form.save()
            data["mensaje"] = "Guardado exitosamente"
        else:
            data["form"] = form
    
    return render(request, 'reserva/agregar_receta.html', data)
    
@csrf_exempt
#muestra todos los medicamentos con su stock actual.
def receta(request, idReceta):
    meds = Medicamento.objects.all()
    recetas = Receta.objects.all()
    receta = Receta.objects.get(idReceta = idReceta)
    detalle, created = DetalleReceta.objects.filter(idReceta = idReceta)
    listaMeds = receta.detallereceta_set.all()
    # listaMeds = DetalleReceta.objects.filter(idreceta = idreceta)
    print('****************',listaMeds)
    context = {'meds':meds, 'listaMeds' :listaMeds, 'recetas':recetas}
    return render(request, 'reserva/receta.html', context) 



def updateMed(request):
    data = json.loads(request.body)
    medId = data['medId']
    action = data['action']
    print(medId)
    print(action)

    # receta = Receta.objects.get(idReceta = idReceta)
    staff = request.user.id
    med = Medicamento.objects.get(codigo=medId)
    # receta, created = Receta.objects.filter(rutMed = staff)

    # detalleReceta, created = DetalleReceta.objects.get_or_create(idReceta=receta, codmed=med)
    
    # if action == 'add':
    #     detalleReceta.cantidad = (detalleReceta.cantidad + 1)
    # elif action == 'remove':
    #     detalleReceta.cantidad = (detalleReceta.cantidad - 1)

    # detalleReceta.save()
    
    # if detalleReceta.cantidad <=0:
    #     detalleReceta.delete()

    return JsonResponse('Med was added', safe=False)

# @csrf_exempt
# def finalizar_receta(request):
#     if request.user.is_authenticated:
#         staff = request.user.id
#         receta, created = Receta.objects.filter(rutMed = staff)
#         listaMeds = receta.detallereceta_set.all()
#     else:
#         listaMeds = []
#     context = {'listaMeds':listaMeds}
#     return render(request, 'reserva/finalizar_receta.html', context) 

#Enviar correo a usuario

def send_email(mail):
    context = {'mail': mail}

    template = get_template('reserva/correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Retiro de medicamentos disponible',
        'Gestor farmacia CESFAM',
        settings.EMAIL_HOST_USER,
        [mail]
    )

    email.attach_alternative(content, 'text/html')
    email.send()

def enviar_correo(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')

        send_email(mail)

        # print('Envio de correo!')

    return render(request, 'reserva/enviar_correo.html', {})
    
def obtener_reservas(codigo):
    #le entregamos un codigo y nos retorna si hay reservas, cuantas y los datos de los pacientes
    reservas = Reserva.objects.get(codigo=codigo)
    for i in reservas:
        telefonos = reservas[i].telefonoPac
        correos = reservas[i].correoPac
        cantidadRes = reservas[i].cantidadReservada
    
    print(telefonos)
    print(correos)
    print(cantidadRes)
    
#prueba carrito2
def crear_receta2(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'reserva/crearRecetas.html', {'medicamentos':medicamentos})

def agregar_medicamento_carrito(request, medicamento_codigo):
    carrito = Carrito(request)
    medicamento = Medicamento.objects.get(codigo=medicamento_codigo)
    carrito.agregar(medicamento)
    return redirect('gestion_medicamentos')

def eliminar_medicamento_carrito(request, medicamento_codigo):
    carrito = Carrito(request)
    medicamento = Medicamento.objects.get(codigo=medicamento_codigo)
    carrito.eliminar(medicamento)
    return redirect('gestion_medicamentos')

def restar_medicamento_carrito(request, medicamento_codigo):
    carrito = Carrito(request)
    medicamento = Medicamento.objects.get(codigo=medicamento_codigo)
    carrito.restar(medicamento)
    return redirect('gestion_medicamentos')

def limpiar_medicamento_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('gestion_medicamentos')

def asignar_receta(request):
    data = {
        'form': AsignarPacienteForm()
    }
    if request.method == 'POST':
        authuser = request.user
        rutMed = authuser.username
        form = AsignarPacienteForm(data=request.POST)
        
        if form.is_valid():
            re = Receta(
                rutPaciente=form.cleaned_data.get("rutPaciente"), 
                fechaReceta=datetime.datetime.now(),
                rutMed=rutMed, 
                observacion=form.cleaned_data.get("observacion"),
                rutReceptor=0,
                entregada=False)
            reId=re.idReceta
            re.save()
            # Carrito.guardar_carrito_bd(reId)
        else:
            data["form"] = form
    limpiar_medicamento_carrito(request)
    return render(request, 'reserva/asignar_receta_paciente.html', data)

