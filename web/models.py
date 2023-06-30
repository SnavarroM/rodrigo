from django.db import models



#!___________________________________________________________________________________________________________________
class Nosotros_Izquierda(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to="nosotros_izquierda",verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Nosotros_Izquierda"
        verbose_name_plural = "Nosotros_izquierda"
        db_table = 'nosotros_izquierda'
        ordering = ["-created"]

    def __str__(self):
        return self.title
#!___________________________________________________________________________________________________________________

class Nosotros_Derecha(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to="nosotros_derecha",verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Nosotros_Derecha"
        verbose_name_plural = "Nosotros_Derecha"
        db_table = 'nosotros_derecha'
        ordering = ["-created"]

    def __str__(self):
        return self.title

#!___________________________________________________________________________________________________________________