from django.contrib import admin

from .models import Nosotros_Derecha,Nosotros_Izquierda

class Nosotros_DerechaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class Nosotros_IzquierdaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Nosotros_Derecha, Nosotros_DerechaAdmin)

admin.site.register(Nosotros_Izquierda, Nosotros_IzquierdaAdmin)