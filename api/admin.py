from django.contrib import admin
from api.models import *


# Register your models here.


class EquipoInline(admin.TabularInline):
    model = Equipo
    extra = 1


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'identificacion', 'email')
    inlines = [EquipoInline, ]


class UsuarioEquipoInline(admin.TabularInline):
    model = UsuarioEquipo
    extra = 3


class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen', 'fecha_creacion', 'lider')
    inlines = [UsuarioEquipoInline, ]


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Equipo, EquipoAdmin)
