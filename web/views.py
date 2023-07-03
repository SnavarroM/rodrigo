from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from .models import Nosotros, Logo
from .forms import ContactForm
from django.core.mail import EmailMessage


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
    

# class ContactFormView(FormView):
#     template_name = "web/contacto.html"
#     form_class = ContactForm

# def contacto(request):
#     return render (request,'formulario.html')


def contacto(request):
    contact_form = ContactForm()
    
    if request.method == 'POST':
        #? estoy enviando los datos desde un formulario
        contact_form = ContactForm(data=request.POST) 
        #? estoy llenado el contact_form de la info del formulario
        
        if contact_form.is_valid(): #? compruebo si esta bien llenado
            
            name = request.POST.get('name', '') #? capturo cada uno de los datos
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            
            #Todo Enviamos el Email
            email = EmailMessage(
               subject,
                "Mensaje enviado por {} <{}>:\n\n{}".format(name,email,message),
                email,
                ["5a9dfd49a5359e@inbox.mailtrap.io"],                
                reply_to=[email],                
            )
            
            try:
                email.send()            
                return redirect('/contacto/?ok') #? esta todo ok
            except:
                return redirect('/contacto/?error') #? Ocurrio un error
    return render(request, 'web/contacto.html',{'form':contact_form})