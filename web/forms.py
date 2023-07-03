from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(initial='Nombre', max_length=100, min_length=5, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nombre'
    }))
    email = forms.EmailField(initial='Email', required=True, max_length=100, widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control'
    }))
    subject = forms.CharField(initial='asunto', max_length=50, min_length=5, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Asunto',
        'class': 'form-control'
    }))
    message = forms.CharField(initial='Mensaje', required=True, widget=forms.Textarea(attrs={
        'placeholder': 'Mensaje',
        'class': 'form-control',
        'rows': 5
    }))
