from rest_framework.routers import DefaultRouter
from biblioteca.views import Biblioteca_ViewSet

app_name = 'biblioteca'

router = DefaultRoute(trailing_slash=False) 
'''Não utiliza barra no final da url'''

router.register(r'biblioteca',Biblioteca_ViewSet)

urlpatterns = routes.urls