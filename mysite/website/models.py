from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.

#Modelo para representar una facultad
class Facultad(models.Model):
	class Meta:
		verbose_name_plural = "facultades"

	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre

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
	escuela = models.ForeignKey(Escuela, blank=True, default=1)
	semestre = models.CharField(max_length=10, choices=SEMESTRES, default='I')
	unique_together = (("codigo", "facultad"),)

	def __str__(self):
		return '%s: %s' % (self.nombre,self.escuela)

# Modelo para el perfil del usuario y otros atributos.
class Perfil(models.Model):

	PREGUNTAS = (('libro','¿Cual es tu libro infantil favorito?'),\
				 ('cancion','¿Cómo se llama tu canción favorita?'),\
				 ('abuelo','¿Cómo se llama tu abuelo paterno?'),\
				 ('abuela','¿Cómo se llama tu abuela materna?'),\
				 ('mascota','¿Como se llamaba tu primera mascota?'),\
				 ('auto','¿Cual es tu marca de autos preferida?'))

	class Meta:
		verbose_name_plural = "perfiles"

	user = models.OneToOneField(User, on_delete = models.CASCADE)
	cedula = models.CharField(max_length=20, default='', unique=True)
	desc = models.TextField(max_length=500,default='' ,blank=True)
		#preguntas y respuestas de seguridad.
	pregunta1 = models.CharField(max_length=15,choices=PREGUNTAS, default='libro')
	respuesta1= models.CharField(max_length=100,default='')
	pregunta2 = models.CharField(max_length=15,choices=PREGUNTAS, default='auto')
	respuesta2= models.CharField(max_length=100,default='')

	facultad = models.ForeignKey(Facultad, default=1)
	escuela = models.ForeignKey(Escuela,default=1)

	carrera = models.CharField(max_length=50,blank=True, default='')

	fallos_login = models.PositiveSmallIntegerField(default=0)
	esta_bloqueado = models.BooleanField(default=False)

	es_supervisor = models.BooleanField(default=False)

	materia = models.ForeignKey(Materia,blank=True, default = 1) #Materia que el usuario supervisor gestiona.

	#falta campo para una imagen del avatar del usuario
	
	def __str__(self):
		return 'Perfil del usuario: %s' % self.user.username

#esta seccion de codigo nos permite crear un modelo perfil
#por cada usuario creado en el sistema automaticamente.
def crear_perfil(sender, **kwargs):
	user = kwargs["instance"]
	if kwargs["created"]:
		user_profile = Perfil(user=user)
		user_profile.save()
		
post_save.connect(crear_perfil, sender=User)

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

#Modelo para representar los recursos descargables de la sección de Descargas.
class Descarga(models.Model):

	TIPOS = (('G','Guia'),('E','Exámen'),('L','Laboratorio'),('B','Libro'))

	nombre = models.CharField(max_length=100)
	tipo = models.CharField(max_length=1, choices=TIPOS, default='G')
	materia = models.ForeignKey(Materia, blank=True)
	fecha_publicado = models.DateTimeField(_('Fecha Publicado'), default=timezone.now)

	def __str__(self):
		return self.nombre

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

#Modelo para representar las solicitudes de asesoría de los usuarios.
#class Asesoria(models.Model):

#	ESTADOS = (('L','Libre'),('P','Pendiente'),('A','Atendida'))

#	titulo = models.CharField(max_length=150)
#	cuerpo = models.TextField(max_length=500)
#	fecha_enviado = models.DateTimeField(_('Fecha Enviado'), default=timezone.now)
#	supervisor = models.ForeignKey(User, blank=True,related_name='asesor',limit_choices_to={'profile__es_supervisor': True})
#	user = models.ForeignKey(User,related_name='asesorado')
#	materia = models.ForeignKey(Materia)
	
#	def __str__(self):
#		return self.titulo

#Modelo para representar las sugerencias de los usuarios.
#class Sugerencia(models.Model):

#	ESTADOS = (('L','Libre'),('P','Pendiente'),('A','Atendida'))
#
#	titulo = models.CharField(max_length=150)
#	cuerpo = models.TextField(max_length=500)
#	fecha_enviado = models.DateTimeField(_('Fecha Enviado'), default=timezone.now)
#	supervisor = models.ForeignKey(User, blank=True,related_name='recipiente',limit_choices_to={'perfil__es_supervisor': True})
#	user = models.ForeignKey(User,related_name='sugeridor')
#
#	def __str__(self):
#		return self.titulo

#Modelo para representar las solicitudes de contacto de los usuarios.
#class Contacto(models.Model):

#	ESTADOS = (('L','Libre'),('P','Pendiente'),('A','Atendida'))

#	titulo = models.CharField(max_length=150)
#	cuerpo = models.TextField(max_length=500)
#	fecha_enviado = models.DateTimeField(_('Fecha Enviado'), default=timezone.now)
#	supervisor = models.ForeignKey(User, blank=True,related_name='supervisor',limit_choices_to={'profile__es_supervisor': True})
#	user = models.ForeignKey(User,related_name='contactador')

#	def __str__(self):
#		return self.titulo



#Modelo abstracto para representar las solicitudes de los usuarios.
#class Solicitud(models.Model):
#	ESTADOS = (('L','Libre'),('P','Pendiente'),('A','Atendida'))
#
#	titulo = models.CharField(max_length=150)
#	cuerpo = models.TextField(max_length=500)
#	fecha_enviado = models.DateTimeField(_('Fecha Enviado'), default=timezone.now)
#	supervisor = models.ForeignKey(User, blank=True,related_name='recipiente')
#
#	def get_username(self):
#		return self.titulo
#	class Meta:
#		abstract = True