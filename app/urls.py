from django.urls import path
# NO OLVIDAR de importar las vistas primero
from .views import home, contacto

urlpatterns = [
    path('', home, name='home'),
    path('contacto/', contacto, name='contacto'),
]