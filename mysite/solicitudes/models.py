from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from website.models import Materia

# Create your models here.

#Modelo para representar las solicitudes de asesoría, contacto y sugerencias de los usuarios.
class Solicitud(models.Model):

	class Meta:
		verbose_name_plural = "solicitudes"

	ESTADOS = (('Libre','Libre'),('Pendiente','Pendiente'),('Atendida','Atendida'))
	TIPOS = (('Asesoría','Asesoría'),('Contacto','Contacto'),('Sugerencia','Sugerencia'))

	nombre = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	telefono = models.CharField(max_length=30, blank=True, default='')
	titulo = models.CharField(max_length=125)
	cuerpo = models.TextField(max_length=255)
	fecha_enviado = models.DateTimeField(_('Fecha Enviado'), default=timezone.now)
	supervisor = models.ForeignKey(User, blank=True, null=True, related_name='recipiente',limit_choices_to={'perfil__es_supervisor': True})
	user = models.ForeignKey(User,related_name='cliente', blank=True, null=True)
	materia = models.ForeignKey(Materia, blank=True, null=True)
	estado = models.CharField(max_length=15, choices=ESTADOS, default='Libre')
	tipo = models.CharField(max_length=15, choices=TIPOS, default='Asesoría')

	def __str__(self):
		return self.titulo
