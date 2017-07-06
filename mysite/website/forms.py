from django import forms
from .models import Perfil
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _ #usado para personalizar las etiquetas de los formularios
from django.core.validators import RegexValidator 		#usado para validar el formato del campo 'cedula'

#Validador para las cedulas
cedula_validator = RegexValidator(r"[VE]-\d+","Ingrese la cédula en el formato indicado.")



# Formulario para iniciar sesión.
class LoginForm(forms.Form):

	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.fields['usernameLogin'].widget = forms.TextInput(attrs={'class':'form-control'})
		self.fields['passwordLogin'].widget = forms.PasswordInput(attrs={'class':'form-control'})
		

	usernameLogin = forms.CharField(label="Usuario", max_length=64)
	passwordLogin = forms.CharField(label="Contraseña") #Este widget nos permite ingresar caracteres ocultos.


# Formulario para registrar un perfil de usuario
class RegisterPerfilForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ['facultad','cedula','pregunta1','respuesta1','pregunta2','respuesta2']
		labels = { 'cedula': _('Cédula'),\
				   'pregunta1': _('Pregunta de seguridad 1'),\
				   'respuesta1': _('Respuesta'),\
				   'pregunta2': _('Pregunta de seguridad 2'),\
				   'respuesta2': _('Respuesta'),\
				 }
		widgets = {'cedula': forms.TextInput(attrs={'placeholder': 'V-12345 ó E-12345','class':'form-control'}),\
				   'pregunta1': forms.TextInput(attrs={'class':'form-control'}),\
				   'pregunta2': forms.TextInput(attrs={'class':'form-control'}),\
				   'respuesta1': forms.TextInput(attrs={'class':'form-control'}),\
				   'respuesta2': forms.TextInput(attrs={'class':'form-control'}),\
				   }

# Formulario para registrar un usuario
class RegisterUserForm(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = "Nombre de Usuario"
		self.fields['password1'].label = "Contraseña"
		self.fields['password2'].label = "Confirmar contraseña"
		self.fields['username'].widget = forms.TextInput(attrs={'class':'form-control'})
		self.fields['password2'].widget = forms.TextInput(attrs={'class':'form-control'})
		self.fields['password1'].widget = forms.TextInput(attrs={'class':'form-control'})
		self.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control'})
		self.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control'})
		self.fields['email'].widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'ejemplo@email.com'})

	
	first_name = forms.CharField(label="Nombre",max_length=30, help_text="Opcional", required = False)
	last_name = forms.CharField(label="Apellido",max_length=30, help_text="Opcional", required = False)
	email = forms.EmailField(label="Correo Electrónico", max_length=254, required=True)

	class Meta:
		model = User
		fields = ('first_name','last_name','email','username','password1','password2',)


		#'password': forms.PasswordInput(),\

#	def __init__(self, *args, **kwargs):
#		super(RegisterUserForm, self).__init__(*args, **kwargs)
#		self.fields['email'].required = True


#	class Meta:
#		model = User
#		fields = ['first_name','last_name','username','password','email']
#		labels = { 'username': _('Usuario'),\
#				   'password': _('Contraseña'),\
#				   'email': _('Email'),\
#				   'first_name': _('Nombre'),\
#				   'last_name':_('Apellido'), 
#				 }
#		widgets = { 'password': forms.PasswordInput(),\
#					'email': forms.TextInput(attrs={'placeholder': 'ejemplo@email.com'}),}
#		#self.fields['email'].required = True
		#email.widget.attrs["required"] = "required"