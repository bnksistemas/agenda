from django.urls import path
# NO OLVIDAR de importar las vistas primero
from .views import home, contacto, agregar_contacto, listar_contacto, modificar_contacto, eliminar_contacto

urlpatterns = [
    path('', home, name='home'),
    path('contacto/', contacto, name="contacto"),
    path('agregar-contacto/', agregar_contacto, name="agregar_contacto"),
    path('listar-contacto/', listar_contacto, name="listar_contacto"),
    path('modificar-contacto/<id>/', modificar_contacto, name="modificar_contacto"),
    path('eliminar-contacto/<id>/', eliminar_contacto, name="eliminar_contacto"),
]
