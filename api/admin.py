from django.contrib import admin
from api.models import *


# Register your models here.


class EquipoInline(admin.TabularInline):
    model = Equipo
    extra = 1


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'identificacion', 'email')
    inlines = [EquipoInline, ]


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Equipo)
