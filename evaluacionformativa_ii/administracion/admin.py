from django.contrib import admin

# Register your models here.

from.models import Autor, Investigacion, Persona, Administrador, Categoria_Inv,Curso,Experiencia,Estudio
admin.site.register(Autor)
admin.site.register(Investigacion)
admin.site.register(Persona)
admin.site.register(Administrador)
admin.site.register(Categoria_Inv)
admin.site.register(Curso)
admin.site.register(Experiencia)
admin.site.register(Estudio)