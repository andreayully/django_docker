from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from api.models import Equipo, UsuarioEquipo
from api.serializers import EquipoSerializer

# Create your views here.


class EquipoCreateView(generics.ListCreateAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

    def perform_create(self, serializer):
        data = self.request.data
        print(data)
        if "integrantes" in data:
            integrantes = data['integrantes']
            del data['integrantes']

            equipo = serializer.save()

            for integrante in integrantes:
                UsuarioEquipo.objects.create(
                    equipo=equipo,
                    usuario_id=integrante)



