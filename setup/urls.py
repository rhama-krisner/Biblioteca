from django.contrib import admin
from django.urls import path
from biblioteca.views import biblioteca

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livros/', biblioteca)
]
