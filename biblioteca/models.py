from django.db import models
import uuid

class Biblioteca_Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, blank=True)
    nome = models.CharField(max_length=70)
    autor = models.CharField(max_length=70)
    isbn = models.IntegerField(blank=True)
    ano_publicacao = models.IntegerField(blank=True)
    genero = models.CharField(max_length=255)
    idioma = models.CharField(max_length=10, default='Unknown', blank=True)
    idioma_original = models.CharField(max_length=10, default='Unknown', blank=True)
    data_cadastro = models.IntegerField(default='Unknown',blank=True)

    def __str__(self):
        return self.nome
        