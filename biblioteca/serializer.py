from rest_framework import serializers
from biblioteca.models import LivroModel

class Biblioteca_Selializer(serializers.ModelSerializer):
    class Meta:
        model = Livro_Model
        fields = '__all__'
