from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.

#Modelo para representar una facultad

class Facultad(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre

# Modelo para el perfil del usuario y otros atributos.

class Perfil(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	desc = models.TextField(max_length=500,default='' ,blank=True)
	facultad = models.ForeignKey(Facultad, blank=True, default=1)
	es_supervisor = models.BooleanField(default=False)
	
	def __str__(self):
		return 'Perfil del usuario: %s' % self.user.username

#esta seccion de codigo nos permite crear un modelo perfil
#por cada usuario creado en el sistema automaticamente.

#def crear_perfil(sender, **kwargs):
#    user = kwargs["instance"]
#    if kwargs["created"]:
#        user_profile = Perfil(user=user)
#        user_profile.save()

#post_save.connect(crear_perfil, sender=User)

#Modelo para representar escuelas de una facultad.
class Escuela(models.Model):

	nombre = models.CharField(max_length=50)
	facultad = models.ForeignKey(Facultad, blank=True, default=1)
	unique_together = (("nombre", "facultad"),)

	def __str__(self):
		return 'Escuela de %s, Facultad de %s' % (self.nombre, self.facultad ,)
		#return self.nombre

#Modelo para representar materias de una facultad.
class Materia(models.Model):

	SEMESTRES = (('electiva', 'Electiva'),('1', 'I'),('2', 'II'),('3', 'III'),('4', 'IV'),('5', 'V'),\
				('6', 'VI'),('7', 'VII'),('8', 'VIII'),('9', 'IX'),('10', 'X'))

	nombre = models.CharField(max_length=100)
	creditos = models.PositiveSmallIntegerField(default=0)
	codigo = models.PositiveSmallIntegerField()
	facultad = models.ForeignKey(Facultad, blank=True, default=1)
	escuela = models.ForeignKey(Escuela, blank=True, default=1)
	semestre = models.CharField(max_length=10, choices=SEMESTRES, default='I')
	unique_together = (("codigo", "facultad"),)

	def __str__(self):
		return '%s: %s' % (self.nombre,self.escuela)

#Modelo para representar posts de la seccion informativa.
class Informacion(models.Model):

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

#Modelo para representar los recursos descargables de la sección de Descargas.
class Descarga(models.Model):

	TIPOS = (('G','Guia'),('E','Exámen'),('L','Laboratorio'),('B','Libro'))


	nombre = models.CharField(max_length=100)
	tipo = models.CharField(max_length=1, choices=TIPOS, default='G')
	materia = models.ForeignKey(Materia, blank=True)
	fecha_publicado = models.DateTimeField(_('Fecha Publicado'), default=timezone.now)