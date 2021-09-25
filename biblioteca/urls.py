from rest_framework import routers
from . import views
from django.urls import path, include


router = routers.DefaultRouter()
router.register('biblioteca', viewset=views.Biblioteca_Views)

urlpatterns = [
    path('', include(router.urls)),
]