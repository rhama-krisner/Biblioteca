from django.shortcuts import render
from rest_framework import viewsets
from biblioteca.serializer import Biblioteca_Serializer
from biblioteca.models import Biblioteca_Model

class Biblioteca_Views(viewsets.ModelViewSet):
    queryset = Biblioteca_Model.objects.all()
    serializer_class = Biblioteca_Serializer
