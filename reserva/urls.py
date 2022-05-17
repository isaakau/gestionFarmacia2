from django.urls import path
from .views import * #importa todo de views

urlpatterns = [
    path('', home, name="home"),
    #se deja el '' vacío, porque esto va a ser lo primero que va a mostrar
    #el segundo parámetro es el views al que le hace referencia 
    path('login/', login, name="login"),
    path('receta/', receta, name="receta"),
    path('crear_receta/', crear_receta, name="crear_receta"),
    path('finalizar_receta/', finalizar_receta, name="finalizar_receta"),
    path('enviar_correo/', enviar_correo, name="enviar_correo"),
]