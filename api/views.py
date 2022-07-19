from api.tasks import create_exame, create_paciente
from registro.models import Exame, Paciente
from django.shortcuts import get_object_or_404
from .serializers import ExameInputSerializer, ExameSerializer,PacienteSerializer,PacienteInputSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    def create(self, request, *args, **kwargs):
        serializer = PacienteInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_paciente.delay(serializer.data)
        return Response("PACIENTE ESTÁ SENDO CRIADO EM SEGUNDO PLANO", status=status.HTTP_201_CREATED)

class ExameViewSet(viewsets.ModelViewSet):
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer

    def get_queryset(self):
        queryset = Exame.objects.all()
        altura = self.request.query_params.get('alturamaiorque')
        if altura is not None:
            queryset = queryset.filter(altura__gt=float(altura))
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = ExameInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_exame.delay(serializer.data)
        return Response("EXAME ESTÁ SENDO CRIADO EM SEGUNDO PLANO", status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = ExameInputSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)



