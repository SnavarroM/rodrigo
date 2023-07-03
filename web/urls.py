
from django.urls import path
from .views import IndexTempleView, NosotrosListView, ServiciosTempleView, contacto

app_name = 'web'

urlpatterns = [
    path('',IndexTempleView.as_view(), name='index'),
    path('contacto/', contacto, name='contacto'),
    path('nosotros/',NosotrosListView.as_view(), name='nosotros'),    
    path('servicios/',ServiciosTempleView.as_view(), name='servicios'),
    
    
]
