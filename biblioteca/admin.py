from django.contrib import admin
from biblioteca.models import Livro_Model

# Register your models here.

class Biblioteca(admin.ModelAdmin):
    list_display = ('id','nome_livro','isbn','autor','ano_publicacao','genero','idioma')
    list_display_links = ('id', 'nome_livro')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Livro_Model, Biblioteca)