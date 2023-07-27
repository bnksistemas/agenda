from django.contrib import admin
from .models import Contacto, Provincia

# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display=["nombre", "domicilio", "telefono"]

admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Provincia)

