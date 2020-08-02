from django.db import models


# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellidos = models.CharField(max_length=50, verbose_name='Apellidos')
    identificacion = models.CharField(max_length=20, verbose_name='identificacion')
    email = models.EmailField(max_length=50, verbose_name='Correo electrónico', null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellidos)


class Equipo(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre del equipo')
    imagen = models.FileField(upload_to='uploads/', verbose_name='Imagen')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    lider = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class UsuarioEquipo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, related_name='integrantes', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}".format(self.usuario, self.equipo)
