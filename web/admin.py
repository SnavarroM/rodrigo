from django.contrib import admin

from .models import Nosotros, Logo

class NosotrosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Nosotros, NosotrosAdmin)

class LogoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Logo, LogoAdmin)

