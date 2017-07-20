from django import forms
from .models import Perfil, Solicitud
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AdminPasswordChangeForm, PasswordChangeForm
from django.utils.translation import ugettext_lazy as _ #usado para personalizar las etiquetas de los formularios
from django.core.validators import RegexValidator 		#usado para validar el formato del campo 'cedula'
from django.contrib.auth import authenticate


#Validador para las cedulas
cedula_validator = RegexValidator(r"[VE]-\d{1,9}","Ingrese una cédula en el formato indicado. V-#### ó E-####", code="invalid")

my_default_errors = {
    'required': 'Por favor rellene este campo.',
    'invalid': 'Por favor ingrese un valor válido.'
}

#Formulario para cambiar la contraseña.
class CambiarPassForm(PasswordChangeForm):
	def __init__(self, *args, **kwargs):
		super(CambiarPassForm, self).__init__(*args, **kwargs)
		self.fields['old_password'].label = "Contraseña actual"
		self.fields['new_password1'].label = "Nueva contraseña"
		self.fields['new_password2'].label = "Confirmar contraseña"

		self.fields['old_password'].widget = forms.PasswordInput(attrs={'class':'form-control'})
		self.fields['new_password1'].widget = forms.PasswordInput(attrs={'class':'form-control'})
		self.fields['new_password2'].widget = forms.PasswordInput(attrs={'class':'form-control'})

class DefinirPassForm(AdminPasswordChangeForm):
	def __init__(self, *args, **kwargs):
		super(DefinirPassForm, self).__init__(*args, **kwargs)
		
		self.fields['password1'].label = "Contraseña"
		self.fields['password2'].label = "Confirmar contraseña"
		self.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control'})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control'})	

# Formulario para recuperar contraseña.
class RecuperarPassForm(forms.Form):

	def __init__(self, *args, **kwargs):
		super(RecuperarPassForm, self).__init__(*args, **kwargs)
		self.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'ejemplo@email.com'})

	email = forms.EmailField(label="Correo Electrónico", max_length=254, required=True)

	def clean(self):
		em = self.cleaned_data.get('email')
		if not User.objects.filter(email=ema).exists():
			raise forms.ValidationError( _("Este correo electrónico no esta en uso."),code='email_not_used')
		return em

# Formulario para iniciar sesión.
class LoginForm(forms.Form):

	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.fields['usernameLogin'].widget = forms.TextInput(attrs={'class':'form-control'})
		self.fields['passwordLogin'].widget = forms.PasswordInput(attrs={'class':'form-control'})
		

	usernameLogin = forms.CharField(label="Usuario", max_length=64, required=True, error_messages=my_default_errors)
	passwordLogin = forms.CharField(label="Contraseña", required=True, error_messages=my_default_errors) #Este widget nos permite ingresar caracteres ocultos.
	
	#Este metodo es llamado para validar el formulario y nos permite verificar si el usuario existe o no.
	def clean(self):
		username = self.cleaned_data.get('usernameLogin')
		password = self.cleaned_data.get('passwordLogin')
		user = authenticate(username=username, password=password)
		sancionado = User.objects.get(username = username)
		perfil = Perfil.objects.get(user = sancionado.id)

		if sancionado and perfil.esta_bloqueado:
			raise forms.ValidationError(_("El usuario ingresado esta bloqueado!"), code='bloqueado')

		if not user:
			if sancionado and not perfil.esta_bloqueado:
				perfil.fallos_login +=  1
				perfil.save()

				if perfil.fallos_login > 4:
					perfil.esta_bloqueado = True
					perfil.fallos_login = 0
				
				perfil.save()
				print (perfil.esta_bloqueado)
			raise forms.ValidationError(_("Información inválida. Por favor intente de nuevo."), code='invalid')
		else:
			perfil.fallos_login = 0
			perfil.save()
		return self.cleaned_data

	def login(self, request):
		username = self.cleaned_data.get('usernameLogin')
		password = self.cleaned_data.get('passwordLogin')
		user = authenticate(username=username, password=password)
		return user

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
		widgets = {'cedula': forms.TextInput(attrs={'placeholder': 'V-12345 ó E-12345','class':'form-control', 'pattern':"[VE]-\d{1,9}"}),\
				   #'pregunta1': forms.TextInput(attrs={'class':'form-control'}),\
				   #'pregunta2': forms.TextInput(attrs={'class':'form-control'}),\
				   'respuesta1': forms.TextInput(attrs={'class':'form-control'}),\
				   'respuesta2': forms.TextInput(attrs={'class':'form-control'}),\
				   }
	
	def clean_cedula(self):
		ci = self.cleaned_data["cedula"]

		if Perfil.objects.filter(cedula=ci).exists():
			raise forms.ValidationError( _("Esta cédula de idetificación ya está en uso, ingrese otra"),code='duplicate_cedula')
		
		return ci


# Formulario para registrar un usuario
class RegisterUserForm(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = "Nombre de Usuario"
		self.fields['password1'].label = "Contraseña"
		self.fields['password2'].label = "Confirmar contraseña"
		self.fields['username'].widget = forms.TextInput(attrs={'class':'form-control'})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control'})
		self.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control'})
		self.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control'})
		self.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control'})
		self.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'ejemplo@email.com'})

	
	first_name = forms.CharField(label="Nombre",max_length=30, help_text="Opcional", required = False)
	last_name = forms.CharField(label="Apellido",max_length=30, help_text="Opcional", required = False)
	email = forms.EmailField(label="Correo Electrónico", max_length=254, required=True)

	class Meta:
		model = User
		fields = ('first_name','last_name','email','username','password1','password2',)

	def clean_username(self):
		username = self.cleaned_data["username"]

		if User.objects.filter(username=username).exists():
			raise forms.ValidationError( _("Este nombre de usuario ya esta en uso, escoga otro."),code='duplicate_username')
		
		return username 


	def clean_email(self):
		#print (self.cleaned_data)
		data = self.cleaned_data['email']
		if User.objects.filter(email=data).exists():
			raise forms.ValidationError(_("Dirección de correo ya esta en uso, escoga otra."),code="invalid")
		return data

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if not password2:
			raise forms.ValidationError("¡Debes repetir tu contraseña!")
		if password1 != password2:
			raise forms.ValidationError("¡Las contraseñas nos son iguales!")
		return password2

# Formulario para realizar una solicitud de contacto.
class ContactanosForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ContactanosForm, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget = forms.TextInput(attrs={'class':'form-control'})
		self.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'ejemplo@email.com'})
		self.fields['telefono'].widget = forms.TextInput(attrs={'class':'form-control'})
		self.fields['titulo'].widget = forms.TextInput(attrs={'class':'form-control'})
		self.fields['cuerpo'].widget = forms.Textarea(attrs={'class':'form-control'})
		



	class Meta:
		model = Solicitud
		fields = ['nombre','email','telefono','titulo','cuerpo']
		labels = { 'nombre': _('Nombre'),\
				   'email': _('Correo electrónico'),\
				   'telefono': _('Teléfono de contacto'),\
				   'titulo': _('Razón de contacto'),\
				   'cuerpo': _('Mensaje'),\
				 }

		#widgets = {'cedula': forms.TextInput(attrs={'placeholder': 'V-12345 ó E-12345','class':'form-control'}),\
				   #'pregunta1': forms.TextInput(attrs={'class':'form-control'}),\
				   #'pregunta2': forms.TextInput(attrs={'class':'form-control'}),\
		#		   'respuesta1': forms.TextInput(attrs={'class':'form-control'}),\
		#		   'respuesta2': forms.TextInput(attrs={'class':'form-control'}),\
		#		   }




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