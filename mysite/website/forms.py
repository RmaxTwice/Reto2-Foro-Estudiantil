from django import forms

# Formulario para iniciar sesión.

class LoginForm(forms.Form):
	username = forms.CharField(label="Usuario", max_length=64)
	password = forms.CharField(label="Contraseña",widget=forms.PasswordInput()) #Este widget nos permite ingresar caracteres ocultos.
		