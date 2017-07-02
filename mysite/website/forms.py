from django import forms
from .models import Perfil
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _ #usado para personalizar las etiquetas de los formularios

# Formulario para iniciar sesión.
class LoginForm(forms.Form):
	username = forms.CharField(label="Usuario", max_length=64)
	password = forms.CharField(label="Contraseña",widget=forms.PasswordInput()) #Este widget nos permite ingresar caracteres ocultos.


# Formulario para registrar un perfil de usuario
class RegisterPerfilForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ['facultad','cedula','pregunta1','respuesta1','pregunta2','respuesta2']

# Formulario para registrar un usuario
class RegisterUserForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = True


	class Meta:
		model = User
		fields = ['first_name','last_name','username','password','email']
		labels = { 'username': _('Usuario'), 'password': _('Contraseña'), 'email': _('Email'),'first_name': _('Nombre'), 'last_name':_('Apellido'), }
		widgets = { 'password': forms.PasswordInput(),}
		#self.fields['email'].required = True
		#email.widget.attrs["required"] = "required"