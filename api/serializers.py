from rest_framework import serializers
from api.models import Equipo, UsuarioEquipo, Usuario
from drf_extra_fields.fields import Base64ImageField


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellidos', 'identificacion', 'email']
        read_only_fields = ['pk']


class EquipoSerializer(serializers.ModelSerializer):
    imagen = Base64ImageField()
    integrantes = serializers.StringRelatedField(many=True, read_only=True)
    #lider = serializers.StringRelatedField()

    class Meta:
        model = Equipo
        fields = ['pk', 'nombre', 'imagen', 'fecha_creacion', 'lider', 'integrantes']
        read_only_fields = ['pk', 'fecha_creacion']


class UsuarioEquipoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    equipo = EquipoSerializer()

    class Meta:
        model = UsuarioEquipo
        fields = ['usuario', 'equipo', 'fecha_creacion']
        read_only_fields = ['pk', 'fecha_creacion']
