from django.db import models



#!________________________________________________Nosotros___________________________________________________________________
class Nosotros(models.Model):
    imagen_uno = models.ImageField(upload_to="Imagen",verbose_name="image_izquierda",blank=True, null=True)    
    title = models.CharField(max_length=200, verbose_name="Título",blank=True, null=True)
    description = models.TextField(verbose_name="Descripción",blank=True, null=True)
    image = models.ImageField(upload_to="Imagen",verbose_name="imagen_derecha")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Nosotros"
        verbose_name_plural = "Nosotros"
        db_table = 'Nosotros'
        ordering = ["-created"]

    def __str__(self):
        return self.title
#!___________________________________________________Logo________________________________________________________________

class Logo(models.Model):
    imagen = models.ImageField(upload_to="Imagen",verbose_name="Logo 130 x 130",blank=True, null=True) 
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "Logo"
        verbose_name_plural = "logo"
        db_table = 'Logo'
        ordering = ["-created"]

#!_________________________________________________________Contacto__________________________________________________________