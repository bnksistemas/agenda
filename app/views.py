from django.shortcuts import render
from .models import Contacto

# Create your views here.
# creo una funcion home que se encarga de enontrar el template home.html
def home(request):

    contactos=Contacto.objects.all()

    data={
        'contactos': contactos
    }

    return render(request, 'app/home.html', data)


def contacto(request):
    return render(request, 'app/contacto.html')
