from ctypes import resize
from dataclasses import field, fields
from pyexpat import model
from django.forms import ValidationError
from rest_framework import serializers

from teacher.models import Aula, Professor

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
        #fields = ('id', 'nome', 'valor_hora', 'descricao', 'foto')

class CadastrarAulaSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length = 255)
    nome = serializers.CharField(max_length = 100)

    def validate_nome(self, value):
        if len(value)<3:
            raise ValidationError("Deve ter pelo menos três caracteres")
        return value
        
class AulaSerializer(serializers.Serializer):
    class Meta:
        model = Aula
        fields = '__all__'