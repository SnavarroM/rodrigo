from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Nosotros_Izquierda

class IndexTempleView(TemplateView):
    template_name = "web/index.html"


class ContactoTemplateView(TemplateView):
    template_name = "web/contacto.html"



class NosotrosListView(ListView):
    model = Nosotros_Izquierda
    context_object_name = 'nosotros'
    template_name = "web/nosotros.html"


class ServiciosTempleView(TemplateView):
    template_name = "web/servicios.html"