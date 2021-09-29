from django.db import models

class BibliotecaModel(models.Model):
    nome_livro = models.CharField(max_length=255, blank=True)
    isbn = models.CharField(max_length=13, blank=True)
    autor = models.CharField(max_length=255)
    ano_publicacao = models.IntegerField(blank=True, null=True)
    genero = models.CharField(max_length=255)
    idioma = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_livro
