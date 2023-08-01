from django.contrib import admin
from .models import Contacto, Provincia, TipoConsulta, Feedback

# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display=["nombre", "domicilio", "telefono"]

admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Provincia)
admin.site.register(TipoConsulta)
admin.site.register(Feedback)

