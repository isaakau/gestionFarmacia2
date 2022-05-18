class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("ca")
        if not carrito:
            self.session["ca"] = {}
            self.carrito = self.session["ca"]
        else:
            self.carrito = carrito
    
    def agregar(self, medicamento):
        id = str(medicamento.codigo)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "id": medicamento.codigo,
                "nombre": medicamento.nombreMed,
                "principio": medicamento.principio,
                "cantidad":1,
            }
        else:
            self.carrito[id]["cantidad"]+=1

        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["ca"]=self.carrito
        self.session.modified = True

    def eliminar(self, medicamento):
        id = str(medicamento.codigo)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, medicamento):
        id = str(medicamento.codigo)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"]-=1
            if self.carrito[id]["cantidad"]<= 0:
                self.elminar(medicamento)

    def limpiar(self):
        self.session["ca"] = {}
        carrito = self.session["ca"]
        self.session.modified = True

    def traer_carrito(request, self):
        carrito = self.session.get("ca")
        print("carrito: ")
        print(carrito)
        return(carrito)

        