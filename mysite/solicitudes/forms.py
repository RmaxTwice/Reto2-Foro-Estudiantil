from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Solicitud

# Formulario para realizar una solicitud de contacto.
class ContactanosForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ContactanosForm, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de contacto'})
		self.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'ejemplo@email.com'})
		self.fields['telefono'].widget = forms.TextInput(attrs={'class':'form-control','pattern':"\d{7,20}",'placeholder':'Teléfono de contacto sin espacios o guiones'})
		self.fields['titulo'].widget = forms.TextInput(attrs={'class':'form-control',})
		self.fields['cuerpo'].widget = forms.Textarea(attrs={'class':'form-control','placeholder':'Escriba su mensaje aquí'})
		



	class Meta:
		model = Solicitud
		fields = ['nombre','email','telefono','titulo','cuerpo']
		labels = { 'nombre': _('Nombre'),\
				   'email': _('Correo electrónico'),\
				   'telefono': _('Teléfono de contacto'),\
				   'titulo': _('Razón de contacto'),\
				   'cuerpo': _('Mensaje'),\
				 }
