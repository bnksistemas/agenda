from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto
from .forms import FeedbackForm, contactoForm
# Create your views here.
# creo una funcion home que se encarga de enontrar el template home.html


def home(request):

    contactos = Contacto.objects.all()

    data = {
        'contactos': contactos
    }

    return render(request, 'app/home.html', data)


def contacto(request):

    return render(request, 'app/contacto.html')


def agregar_contacto(request):

    data = {
        'form': contactoForm()
    }
    if request.method == 'POST':
        formulario = contactoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'app/contacto/agregar.html', data)

def listar_contacto(request):
    contactos=Contacto.objects.all()

    data={
        'contactos': contactos
    }

    return render(request, 'app/contacto/listar.html', data)

def modificar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    data = {
        'form': contactoForm(instance = contacto)
    }
    if request.method == 'POST':
        formulario = contactoForm(data=request.POST, instance=contacto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect( to="listar_contacto")
        data["form"]=formulario
    return render(request, 'app/contacto/modificar.html',data)

def eliminar_contacto(request, id):
    contacto=get_object_or_404(Contacto, id=id)
    contacto.delete()
    return redirect( to="listar_contacto")
   

