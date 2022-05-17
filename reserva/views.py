from django.conf import settings
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
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