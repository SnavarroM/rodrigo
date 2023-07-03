from django.contrib import admin

from .models import Nosotros, Logo

class NosotrosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Nosotros, NosotrosAdmin)

# class LogoAdmin(admin.ModelAdmin):
#     readonly_fields = ('created', 'updated')


# admin.site.register(Logo, LogoAdmin)

admin.site.site_header = '2GBOOST'
admin.site.index_title = 'Panel de control 2gboost.cl'
admin.site.site_title = 'Esta ingresando a 2gboost'