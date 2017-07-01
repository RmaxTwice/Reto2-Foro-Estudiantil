from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

#Modelo para representar una facultad

class Facultad(models.Model):
	nombre = models.TextField(max_length=50);

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


