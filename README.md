# gestionFarmacia2
Proyecto para el ramo de Integración de plataformas
Consiste en crear una página web donde los médicos puedan ver el stock de medicamentos disponibles en la farmacia del cesfam y recetarlos para los pacientes.
En caso de no haber medicamento, debe poder dejar reservado el medicamento para el próximo stock.
Para este desarrollo se utiliza el framework django python, implementando las vistas en html, css y bootstrap
Se implementan dos APIs, para poder enviar mensajes de correo electrónico o whatsapp a los pacientes avisando que llego su medicamento.

PASOS CREACIÓN PROYECTO
1. Se elige la carpeta y se crea el proyecto con django-admin startproject nombredelproyecto.
2. Una vez creado, se crea una app para el proyecto con python manage.py startapp nombredelaapp
3. Es importante que dentro de la app se cree una carpeta llamada templates, que es el directorio por defecto donde django busca las vistas, aqui se dejan los
html del proyecto.
4. Luego para vincular estas vistas al proyecto, debemos ir al archivo views.py dentro de la carpeta de nuestra aplicación y llamar "form django.shortcuts import render"
y después definir como se llama cada vista como por ejemplo: 
    def home(request):
        return render(request, '/index.html')
5. Ya hecho esto, nos vamos al archivo urls.py (si no existe, crearlo) dentro de la carpeta de la aplicación y se escribe el siguiente código:
    from django.urls import path
    from .views import * #importa todo de views

    urlpatterns = [
        path('', home, name="home"),
        path('login', login, name="login"),
    ]
para poder llamar estas vistas.
6. Luego nos vamos al archivo urls.py de la carpeta principal del proyecto y escribimos este proyecto
    from django.contrib import admin
    from django.urls import path, include #aqui se llama adicionalmente al include para usarlo mas abajo

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('reserva.urls')), #esto permite acceder a las vistas html creadas en la app reserva
    ]

INSTRUCCIONES PARA LA BASE DE DATOS
1. Se debe crear el modelo en models.py. Aquí se escriben las tablas siguiendo el formato de django, especificando ciertas opciones.
2. Luego de que tenemos el modelo listo debemos ejecutar el comando python manage.py makemigrations nombreapp.
3. A continuación se ejecuta el comando python manage.py migrate nombreapp que creará efectivamente las tablas.
4. Luego de esto podemos activar el django admin para gestionar la bd, que se hace creando un superusuario con el comando python manage.py createsuperuser.
La contraseña debe tener al menos 8 caracteres y al escribirla no la vemos en la terminal. Con esto, el framework ya sabe que estamos creando un usuario para
acceder al admin. (la que se creó para probar es admin y la clave es admin)(se crearon dos usuarios de prueba: 102366584-4 medicoprueba1 y 7523625-4 farmaciaprueba1)
5. Para utilizar el admin se escribe url/admin y se logea con la cuenta que creamos anteriormente. De esta forma visualizaremos las tablas que genera django automáticamente
para los usuarios y los grupos.
6. Luego, para poder ver nuestrar tablas propias en este admin, necesitamos ir al archivo admin.py y escribir la linea "from .models import" y a continuación, cada una de las
tablas que creamos. Para que se muestren debemos escribir otra linea debajo que diga admin.site.register(nombre de la tabla).
7. Para cambiar el idioma del admin, nos vamos a settings.py y buscamos la linea LANGUAGE_CODE='en-us' y cambiamos en-us por es.
8. El TIME_ZONE en settings, se cambia a partir de una base de datos global que se puede encontrar en: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones y se copia la información que aparece en la columna TZ database name. Esto se hace porque tenemos una fecha que se guarda automáticamente en la receta, para que muestre la fecha y hora
correctas.


Usuarios para probar los correos
1. admin admin -> envia correo a Isabella
2. paty paty1234
3. mrcutux cutu1234
4. fisko francisco1234