from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader




# Views de la app principal 'website' van aca.
def index(request):
	return render(request, 'website/index_noauth.html')

def logmein(request):
	return render(request, 'website/index_user.html')

def adminview(request):
	return render(request, 'website/index_user_admin.html')

def registrar(request):
	return render(request, 'website/registrar.html')

def login(request):
	#aca se procesará la solicitud de login.
	return render(request, 'website/index.html')

def contacto(request):
	return render(request, 'website/contacto.html')

def descargas(request):
	return render(request, 'website/descargas.html')

def descargas_materia(request):
	return render(request, 'website/descarga_detalle.html')

def informacion(request):
	return render(request, 'website/informacion.html')

def pedir_asesoria(request):
	return render(request, 'website/pedir_asesoria.html')

def perfil(request):
	return render(request, 'website/perfil.html')

def sugerencia(request):
	return render(request, 'website/sugerencia.html')

def administrar_descargas(request):
	return render(request, 'website/administrar_descargas.html')

def administrar_solicitudes(request):
	return render(request, 'website/administrar_solicitudes.html')

def administrar_informacion(request):
	return render(request, 'website/administrar_informacion.html')

