from .Carrito import *

def guardar_receta(request):
    if request.user.is_authenticated:
        if "ca" in request.session.keys():
            for key, value in request.session["ca"].items():
                print(value["id"])
                carrito ={
                    "id":value["id"],
                    "nombre": value["nombre"],
                    "principio": value["principio"],
                    "cantidad":value["cantidad"]
                }
    return{"ca"}