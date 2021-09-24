from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('biblioteca/v1/', include('biblioteca.urls', namespace='biblioteca')),
    path('biblioteca-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
