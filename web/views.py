from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from .models import Nosotros, Logo
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.core.mail import send_mail

import logging
logger = logging.getLogger(__name__)


class IndexTempleView(TemplateView):
    template_name = "web/index.html"


# class ContactoTemplateView(TemplateView):
#     template_name = "web/contacto.html"


class NosotrosListView(ListView):
    model = Nosotros
    context_object_name = 'nosotros'
    template_name = "web/nosotros.html"



class ServiciosTempleView(TemplateView):
    template_name = "web/servicios.html"


class LogoTemplateView(TemplateView):
    model = Logo
    context_object_name = 'logo'
    template_name = "menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.first()
        return context




#!_________________________________________________________________________________________________

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                'Nuevo mensaje del formulario de contacto',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                'contacto@2gboost.cl',
                ['contacto@2gboost.cl'],
                fail_silently=False,
            )
            # return render(request, 'contact_success.html')
            return redirect('/contacto/?error')
    else:
        form = ContactForm()
    return render(request, 'web/contacto.html', {'form': form})