from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.db import connection, transaction
from django.forms.models import inlineformset_factory
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext, loader
from django.template.loader import render_to_string
from social_django.models import UserSocialAuth
from .forms import LoginForm, CambiarPassForm, DefinirPassForm, RegisterPerfilForm, RegisterUserForm, RecuperarPassForm, EditarUserForm, EditarPerfilForm
from .models import Perfil



# Views de la app principal 'website' van aca.
def index(request):
	if request.user.is_authenticated:
		if request.user.perfil.es_supervisor:
			return render(request, 'website/index_user.html',{'base_template':'website/base_admin.html'})
		else:
			return render(request, 'website/index_user.html',{'base_template':'website/base_usuario.html'})
	else:
		loginf = LoginForm()	
		return render(request, 'website/index_noauth.html', {'loginf': loginf})

# View para autenticar usuarios e iniciar sesión
def logmein(request):
	
	form = LoginForm(request.POST or None)

	if request.POST and form.is_valid():
		user = form.login(request)
		if user:
			login(request, user)
			return HttpResponseRedirect('/')
	return render(request, 'website/index_noauth.html', {'loginf': form })

	
# View para cerrar la sesión de usuarios
def logmeout(request):
	logout(request)
	return HttpResponseRedirect('/')


	return render(request, 'website/index_noauth.html')


# View para desplegar el formulario de registro de usuarios y atender las peticiones de registro
def registrar(request):
	loginf = LoginForm()

	if request.method == 'POST':
		ruf = RegisterUserForm(request.POST, prefix='user')
		rpf = RegisterPerfilForm(request.POST, prefix='userprofile')
		if ruf.is_valid() * rpf.is_valid():
			user = ruf.save()
			userprofile = user.perfil
			print (userprofile)
			userprofile.cedula = rpf.cleaned_data['cedula']
			userprofile.facultad = rpf.cleaned_data['facultad']
			userprofile.pregunta1 = rpf.cleaned_data['pregunta1']
			userprofile.respuesta1 = rpf.cleaned_data['respuesta1']
			userprofile.pregunta2 = rpf.cleaned_data['pregunta2']
			userprofile.respuesta2 = rpf.cleaned_data['respuesta2']
			userprofile.save()

			# Ahora una vez creado el usuario y su perfil procederemos a enviarle un mensaje
			# al email indicado con sus credenciales.
			context = {'username':ruf.cleaned_data['username'] ,'password':ruf.cleaned_data['password1']}
			
			msg_plain = render_to_string('registration/user_register_email.txt', context)
			msg_html = render_to_string('registration/user_register_email.html', context)
			
			send_mail(
					'Bienvenido a Foro-Estudiantil!', 	#titulo
					msg_plain,							#mensaje txt
					'foroestudiantil2@gmail.com',		#email de envio
					[user.email],						#destinatario
					html_message=msg_html,				#mensaje en html
					)

			
			return HttpResponseRedirect('/')
		else:
			return render(request,'website/registrar.html', {'registeruserform':ruf, 'registerperfilform':rpf,'loginf': loginf})
	else:
		ruf = RegisterUserForm(prefix='user')
		rpf = RegisterPerfilForm(prefix='userprofile')
			#Si un usuario con sesión iniciada llega a esta página, se le cerrará la sesión.
		if request.user.is_authenticated:
			logout(request)

		return render(request, 'website/registrar.html', {'registeruserform':ruf, 'registerperfilform':rpf,'loginf': loginf})

def recuperar_pass(request):

	if request.method == 'POST':
		recuperarf = RecuperarPassForm(request.POST or None)
		if recuperarf.is_valid():
			print (recuperarf.email)	
		return HttpResponseRedirect('/')
	loginf = LoginForm()
	recuperarf = RecuperarPassForm()
	return render(request, 'website/recuperar_contraseña.html', {'recuperarf':recuperarf, 'loginf':loginf})

def desbloquear_cuenta(request):
	user = request.user
	user.perfil.esta_bloqueado = False
	user.save()
	return HttpResponseRedirect('/')

	
@login_required(login_url='/') 
def perfil(request):
	contexto_comun = {'nombre': request.user.first_name,\
	  				   'apellido': request.user.last_name,\
	  				   'email': request.user.email,\
	  				   'facultad': request.user.perfil.facultad,\
	  				   'desc': request.user.perfil.desc,\
	  				   'base_template':'website/base_usuario.html'\
	  				  }

	contexto_admin = {'nombre': request.user.first_name,\
	  				   'apellido': request.user.last_name,\
	  				   'email': request.user.email,\
	  				   'facultad': request.user.perfil.facultad,\
	  				   'desc': request.user.perfil.desc,\
	  				   'base_template':'website/base_admin.html'\
	  				  }

	if request.user.perfil.es_supervisor:
		return render(request, 'website/perfil.html',contexto_admin)
	else:
		return render(request, 'website/perfil.html',contexto_comun)

# Vista que se encarga de el manejo de la edicion de los perfiles de usuario.
@login_required(login_url='/') 
def perfil_editar(request):
	user_form =	EditarUserForm(instance=request.user)
	perfil_form = EditarPerfilForm(instance=request.user.perfil)

	if request.user.perfil.es_supervisor:
		return render(request, 'website/perfil_editar.html',{'base_template':'website/base_admin.html', 'uf':user_form,'pf':perfil_form })
	else:
		return render(request, 'website/perfil_editar.html',{'base_template':'website/base_usuario.html', 'uf':user_form,'pf':perfil_form })


@login_required
def opciones(request):
	user = request.user

	try:
		facebook_login = user.social_auth.get(provider='facebook')
	except UserSocialAuth.DoesNotExist:
		facebook_login = None

	can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

	if request.user.perfil.es_supervisor:
		return render(request, 'website/opciones.html',{'base_template':'website/base_admin.html','facebook_login': facebook_login,'can_disconnect': can_disconnect})
	else:
		return render(request, 'website/opciones.html',{'base_template':'website/base_usuario.html','facebook_login': facebook_login,'can_disconnect': can_disconnect})


@login_required
def password(request):
	if request.user.has_usable_password():
		PasswordForm = CambiarPassForm
	else:
		PasswordForm = DefinirPassForm

	if request.method == 'POST':
		form = PasswordForm(request.user, request.POST)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			#messages.success(request, 'Tu contraseña ha sido actualizada exitosamente!')
			return redirect('/opciones')
	else:
		form = PasswordForm(request.user)

	if request.user.perfil.es_supervisor:
		return render(request, 'website/password.html',{'base_template':'website/base_admin.html','form': form})
	else:
		return render(request, 'website/password.html',{'base_template':'website/base_usuario.html','form': form})
