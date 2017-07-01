from django.contrib import admin
from .models import Facultad, Perfil, Materia, Escuela, Informacion, Descarga



# Register your models here.

admin.site.register(Facultad)
admin.site.register(Perfil)
admin.site.register(Escuela)
admin.site.register(Materia)
admin.site.register(Informacion)
admin.site.register(Descarga)