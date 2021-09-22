from rest_framework import serializers
from biblioteca.models import Biblioteca_Model

class Biblioteca_Serializer(serializer.Biblioteca_Model):
    class Meta:
        models = Biblioteca_Model
        fields = '__all__'