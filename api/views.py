from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from api.models import Equipo, UsuarioEquipo
from api.serializers import EquipoSerializer
from django.core.mail import send_mail


# Create your views here.


class EquipoCreateView(generics.ListCreateAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

    def perform_create(self, serializer):
        data = self.request.data
        if "integrantes" in data:
            integrantes = data['integrantes']
            del data['integrantes']

            equipo = serializer.save()

            for integrante in integrantes:
                UsuarioEquipo.objects.create(
                    equipo=equipo,
                    usuario_id=integrante)

            self.enviar_correo(equipo)

    def enviar_correo(self, equipo):
        url_equipo = "http://localhost:8000/equipo/{}/".format(equipo.id)
        detalle = "Se creo el equipo {} el dia {} para mas detalle ingrese a {}".format(equipo.nombre,
                                                                                        equipo.fecha_creacion,
                                                                                        url_equipo)
        send_mail(
            'Se creo el Equipo {}'.format(equipo.nombre),
            detalle,
            'from@example.com',
            [equipo.lider.email],
            fail_silently=False,
        )


class EquipoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

    def perform_update(self, serializer):
        data = self.request.data
        if "integrantes" in data:
            integrantes = data['integrantes']
            del data['integrantes']

            equipo = serializer.save()

            for integrante in integrantes:
                if not UsuarioEquipo.objects.filter(equipo=equipo, usuario=integrante).exists():
                    UsuarioEquipo.objects.create(
                        equipo=equipo,
                        usuario_id=integrante)

            self.enviar_correo(equipo)

    def enviar_correo(self, equipo):
        url_equipo = "http://localhost:8000/equipo/{}/".format(equipo.id)
        detalle = "Se creo el equipo {} el dia {} para mas detalle ingrese a {}".format(equipo.nombre,
                                                                                        equipo.fecha_creacion,
                                                                                        url_equipo)
        send_mail(
            'Se actualizo el Equipo {}'.format(equipo.nombre),
            detalle,
            'from@example.com',
            [equipo.lider.email],
            fail_silently=False,
        )
