
from celery import shared_task
from registro.models import Paciente,Exame


@shared_task
def create_exame(object):
    object["paciente"] = Paciente.objects.get(pk=object["paciente"])
    Exame.objects.create(**object)


@shared_task
def create_paciente(object):
    Paciente.objects.create(**object)
   

    
