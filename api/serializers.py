from rest_framework import serializers
from api.utils import calculateAge
from registro.models import Exame,Paciente
from datetime import date

class PacienteSerializer(serializers.ModelSerializer):
    idade = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Paciente
        fields = (
            "id",
            "nome",
            "data_nascimento",
            "endereco",
            "idade",
        )

    def get_idade(self, obj):
        if  hasattr(obj,'data_nascimento'):
            return calculateAge(obj.data_nascimento)
        return calculateAge(obj['data_nascimento'])

        
class PacienteInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = (
            "id",
            "nome",
            "data_nascimento",
            "endereco",
        )

class ExameInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exame
        fields = (
            "id",
            "paciente",
            "profissional",
            "data_exame",
            "peso",
            "altura",
        )
    
class ExameSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer()

    class Meta:
        model = Exame
        fields = (
            "id",
            "paciente",
            "profissional",
            "data_exame",
            "peso",
            "altura",
        )


   