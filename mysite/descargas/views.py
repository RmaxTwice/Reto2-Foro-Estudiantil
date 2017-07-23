from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from website.models import Materia, Facultad
# Create your views here.

@login_required(login_url='/') 
def descargas(request):
	if request.user.perfil.es_supervisor:
		return render(request, 'descargas/descargas.html',{'base_template':'descargas/base_admin.html'})
	else:
		return render(request, 'descargas/descargas.html',{'base_template':'descargas/base_usuario.html'})

@login_required(login_url='/') 
def descargas_materia(request):
	if request.user.perfil.es_supervisor:
		return render(request, 'descargas/descarga_detalle.html',{'base_template':'descargas/base_admin.html'})
	else:
		return render(request, 'descargas/descarga_detalle.html',{'base_template':'descargas/base_usuario.html'})