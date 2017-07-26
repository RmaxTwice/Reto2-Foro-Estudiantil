from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from website.models import Facultad
# Create your models here.

#Modelo para representar posts de la seccion informativa.
class Informacion(models.Model):

	class Meta:
		verbose_name_plural = "informaciones"


	TEMAS = (('G','General'),('T','Tesis'),('S','Seminario'),('SC','Servicio Comunitario'),\
			('P','Pasantías'),('R','Reincorporaciones'))

	facultad = models.ForeignKey(Facultad, blank=True, default=1)
	titulo = models.CharField(max_length=200)
	cuerpo = models.TextField(max_length=1000)
	tema = models.CharField(max_length=2, choices=TEMAS, default='G')
	activo = models.BooleanField(default=True)
	fecha_publicado = models.DateTimeField(_('Fecha Publicado'), default=timezone.now)


	def __str__(self):
		return '%s: %s' % (self.facultad,self.titulo)
