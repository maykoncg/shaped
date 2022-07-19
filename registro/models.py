from django.db import models
import uuid

class BaseModel(models.Model):
    id = models.UUIDField(
        verbose_name="Indentificador",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    created_at = models.DateTimeField(verbose_name="Criado às", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Atualizado às", auto_now=True)
    deleted_at = models.DateTimeField(
        verbose_name="Deletado às", blank=True, null=True, default=None
    )

    class Meta:
        abstract = True
        ordering = ["-created_at"]

# Create your models here.
class Paciente(BaseModel):
    nome = models.CharField(
        verbose_name="Nome", max_length=80
    )
    data_nascimento = models.DateField(
        verbose_name="Data de nascimento"
    )
    endereco = models.CharField(
        verbose_name="Endereço", max_length=255
    )

class Exame(BaseModel):
    paciente = models.ForeignKey(Paciente,verbose_name="Paciente",on_delete=models.CASCADE)
    profissional = models.CharField(
        verbose_name="Nome do profissional", max_length=80
    )
    data_exame = models.DateField(
        verbose_name="Data do exame"
    )
    peso = models.DecimalField(
        verbose_name="Peso (Kg)",max_digits=11,
        decimal_places=3,
    )
    altura = models.DecimalField(
        verbose_name="Altura (m)",max_digits=11,
        decimal_places=2,
    )