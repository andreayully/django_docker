# django_docker

## Team Work

Prototipo funcional que permite organizar equipos de trabajo.
Permite crear y administrat los equipos desde el admin de Django.
CRUD para el modelo de Equipo asi como para agregar integrantes desde apis por medio de DRF que permite almacenar imagenes codificadas en Base64
y envia correo al momento de ser creado o actualizado un equipo de trabajo.

### Para ejecutar de manera local

* Pre-requisitos Python 3.+ y Virtualenv
1. Crear ambiente virtual virtualenv  y activar el ambiente 
2. Clonar el proyecto **git clone https://github.com/andreayully/django_docker.git**
3. Desde la carpeta raiz **pip install -R requirements.txt**
4. Cambar las configuraciones en setting.py para la base de datos y envio de correo
5. Correr migraciones
6. Crear superusuario **python manage.py createsuperuser**
7. Runserver python manage.py runserver http://127.0.0.1:8000/admin/

### Características
* Django 2.2.14
* djangorestframework 3.11.0
* Base de datos Postgresql

### Contenedor Docker
Cuenta con Dockerfile y docker-compose.yml para ser ejecutado en un contenedor docker segun [documentacion de Docker](https://docs.docker.com/compose/django/)
