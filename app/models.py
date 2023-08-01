from django.db import models

# Create your models here.


class Provincia(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"
        db_table = "provincia"


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to='contacto_imagenes/',
                               null=True, blank=True, default='contacto_imagenes/default_contacto.jpg',
                               verbose_name='Imagen de la persona')
    provincia = models.ForeignKey(
        Provincia, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        db_table = "contacto"


class TipoConsulta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Feedback(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.ForeignKey(TipoConsulta, on_delete=models.CASCADE)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"
        db_table = "feedback"


    def __str__(self):
        return self.nombre
