from django.urls import path
from .views import * #importa todo de views

urlpatterns = [
    path('', home, name="home"),
    #se deja el '' vacío, porque esto va a ser lo primero que va a mostrar
    #el segundo parámetro es el views al que le hace referencia 
    path('receta/', receta, name="receta"),
    path('gestion_medicamentos/', gestion_medicamentos, name="gestion_medicamentos"),
    path('crear_medicamento/', crear_medicamento, name="crear_medicamento"),
    path('modificar_medicamento/<codigo>/', modificar_medicamento, name="modificar_medicamento"),
    path('crear_receta/', crear_receta, name="crear_receta"),
    path('finalizar_receta/', finalizar_receta, name="finalizar_receta"),

]