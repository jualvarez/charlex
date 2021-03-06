from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins, permissions

from charlas.serializers import (
    UsuarioSerializer,
    OradorSerializer,
    LugarSerializer,
    CharlaSerializer,
    UsuarioCharlaSerializer,
    FotoCharlaSerializer
)

from charlas.models import (
    Orador,
    Lugar,
    Charla,
    UsuarioCharla,
    FotoCharla
)

User = get_user_model()


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (permissions.AllowAny,)


class OradorViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Orador.objects.all()
    serializer_class = OradorSerializer


class LugarViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Lugar.objects.all()
    serializer_class = LugarSerializer


class CharlaViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Charla.objects.all()
    serializer_class = CharlaSerializer
    filter_fields = ('orador',)


class UsuarioCharlaViewSet(viewsets.ModelViewSet):
    queryset = UsuarioCharla.objects.all()
    serializer_class = UsuarioCharlaSerializer
    filter_fields = ('charla', 'usuario')

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get('solo_yo'):
            return queryset.filter(usuario=self.request.user)

        return queryset


class FotoCharlaViewSet(viewsets.ModelViewSet):
    queryset = FotoCharla.objects.all()
    serializer_class = FotoCharlaSerializer
    filter_fields = ('charla', 'usuario')
