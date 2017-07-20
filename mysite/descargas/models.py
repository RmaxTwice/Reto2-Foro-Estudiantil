from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from website.models import Materia

# Create your models here.

#Modelo para representar los recursos descargables de la sección de Descargas.
class Descarga(models.Model):

	TIPOS = (('G','Guia'),('E','Exámen'),('L','Laboratorio'),('B','Libro'))

	nombre = models.CharField(max_length=100)
	tipo = models.CharField(max_length=1, choices=TIPOS, default='G')
	materia = models.ForeignKey(Materia, blank=True)
	fecha_publicado = models.DateTimeField(_('Fecha Publicado'), default=timezone.now)

	def __str__(self):
		return self.nombre
