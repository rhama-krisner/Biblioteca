from biblioteca.serializer import Biblioteca_Serializer
from rest_framework import viewsets, permissions
from biblioteca.models import Biblioteca_Model

class Biblioteca_ViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca_Model.objects.all()
    serializer = Biblioteca_Serializer
    permission_classes = [permissions.IsAuthenticated]