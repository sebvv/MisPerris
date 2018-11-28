from django.db import models

# Create your models here.

class Region(models.Model):
    nombre_region = models.CharField(max_length=200,unique=True,verbose_name="Region")

    def __str__(self):
        return self.nombre_region

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"

class Vivienda(models.Model):
    tipo_vivienda = models.CharField(max_length=30,verbose_name="Tipo Vivienda")

    def __str__(self):
        return self.tipo_vivienda

    class Meta:
        verbose_name = "Vivienda"
        verbose_name_plural = "Viviendas"

class Comuna(models.Model):
    nombre_comuna = models.CharField(max_length=200,verbose_name="Comuna")
    #clave foranea
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_comuna

    class Meta:
        verbose_name = "Comuna"
        verbose_name_plural = "Comunas"




class Formulario(models.Model):
    rut_postulante = models.CharField(max_length=10,unique=True,verbose_name="Rut postulante")
    nombre_postulante = models.CharField(max_length=150,verbose_name="nombre")
    fecha_nacimiento  =   models.DateField(verbose_name="fecha nacimiento")
    correo  =   models.EmailField(verbose_name="Correo")
    telefono    =   models.IntegerField(verbose_name="telefono")
    
    #clave foranea
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.rut_postulante

    class Meta:
        verbose_name = "Formulario"
        verbose_name_plural = "Formulario"
  

class Genero(models.Model):
    genero = models.CharField(max_length=1,unique=True, verbose_name="Genero")

    def __str__(self):
        return self.genero

    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"

class Raza(models.Model):
    raza_mascota = models.CharField(max_length=25, verbose_name="Raza")

    def __str__(self):
        return self.raza_mascota

    class Meta:
        verbose_name = "Raza"
        verbose_name_plural = "Razas"

        
class Estado(models.Model):
    estado = models.CharField(max_length=25,verbose_name="Estado")

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

class Mascotas(models.Model):

    nombre_mascota = models.CharField(max_length=150,verbose_name="nombre Mascota")
    fecha_ingreso  =   models.DateField(verbose_name="fecha Ingreso")
    fecha_nacimiento  =   models.DateField(verbose_name="fecha nacimiento")
    foto = models.ImageField(upload_to="mascotas",null=False,verbose_name="Foto Mascota")
    #claves foraneas
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_mascota

    class Meta:
        verbose_name = "mascota"
        verbose_name_plural = "mascotas"