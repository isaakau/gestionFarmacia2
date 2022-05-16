from django.urls import path
from .views import * #importa todo de views

urlpatterns = [
    path('', home, name="home"),
    #se deja el '' vacío, porque esto va a ser lo primero que va a mostrar
    #el segundo parámetro es el views al que le hace referencia 
    path('login/', login, name="login"),
    path('receta/', receta, name="receta"),
    path('enviar_receta/', enviar_receta, name="enviar_receta"),
]