from django.contrib import admin

# Register your models here.
from .models import Comuna,Region,Formulario,Mascotas,Genero,Estado,Vivienda,Raza

# Register your models here.

class FormularioAdmin(admin.ModelAdmin):
    list_display = ('rut_postulante','nombre_postulante','fecha_nacimiento','correo','telefono','region','comuna','vivienda')
    search_fields = ['rut_postulante','region']
    #agregamos un filtro personalizado en el admin
    list_filter = ('rut_postulante',)

class MascotasAdmin(admin.ModelAdmin):

    list_display = ('nombre_mascota','fecha_ingreso','fecha_nacimiento','estado','genero','raza','foto')
    search_fields = ['nombre_mascota','raza']
    #agregamos un filtro personalizado en el admin
    list_filter = ('nombre_mascota',)
    

admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Vivienda)
admin.site.register(Formulario,FormularioAdmin)
admin.site.register(Mascotas,MascotasAdmin)
admin.site.register(Raza)
admin.site.register(Genero)
admin.site.register(Estado)

