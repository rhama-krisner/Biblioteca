from rest_framework import serializers
from biblioteca.models import BibliotecaModel

class Biblioteca_Selializer(serializers.ModelSerializer):
    class Meta:
        model = BibliotecaModel
        fields = '__all__'
