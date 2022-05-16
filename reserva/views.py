from django.shortcuts import render

# Aquí es donde declaramos nuestras vistas personalizadas, a partir de los html que tenemos en la carpeta templates
#en el codigo de abajo solo se pone reserva porque la función busca automáticamente la carpeta templates
def home(request):
    return render(request, 'reserva/home.html') 
#lo que hicimos fue definir como home, el archivo html que se llama home
#esto quiere decir que cuando la url de la pagina no tenga nada después del /, nos redirecciona a esta pagina home
def login(request):
    return render(request, 'reserva/login.html') 

def receta(request):
    context = {}
    return render(request, 'reserva/receta.html', context) 

def enviar_receta(request):
    context = {}
    return render(request, 'reserva/enviar_receta.html', context) 