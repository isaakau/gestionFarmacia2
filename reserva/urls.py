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
    path('listar_recetas', listar_recetas, name="listar_recetas"),
    path('crear_receta/', crear_receta, name="crear_receta"),
    path('finalizar_receta/', finalizar_receta, name="finalizar_receta"),
    path('enviar_correo/', enviar_correo, name="enviar_correo"),
    #prueba carrito2
    path('crear_receta2', crear_receta2, name="crear_receta2"), 
    path('agregar/<int:medicamento_codigo>/', agregar_medicamento_carrito, name="agregar_medicamento_carrito"),
    path('eliminar/<int:medicamento_codigo>/', eliminar_medicamento_carrito, name="eliminar_medicamento_carrito"),
    path('restar/<int:medicamento_codigo>/', restar_medicamento_carrito, name="restar_medicamento_carrito"),
    path('limpiar/', limpiar_medicamento_carrito, name="limpiar_medicamento_carrito"),
    #poblar tablas
    path('asignar_receta/', asignar_receta, name="asignar_receta"),

]