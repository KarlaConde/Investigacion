from rest_framework import serializers
from.models import Autor, Investigacion, Persona, Administrador

#Completar los demas servicios

class InvestigacionSerializers(serializers.ModelSerializer):
    class Meta:
        model= Investigacion
        fields= '__all__'

class AutorSerializers(serializers.ModelSerializer):
    class Meta:
        model= Autor
        fields= '__all__'

class AdministradorSerializers(serializers.ModelSerializer):
    class Meta:
        model= Administrador
        fields= '__all__'