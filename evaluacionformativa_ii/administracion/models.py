from distutils.command.upload import upload
from pyexpat import model
from random import choices
from secrets import choice
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify

# Create your models here.
class Categoria_Inv(models.Model):
    
    categoria_investigacion=models.CharField(verbose_name="Categoria",max_length=150)
    descripcion=models.TextField()
    foto = models.ImageField(upload_to="fotos_categorías/", verbose_name="Foto categoria", null = True, blank=True)

    
    class meta:
        verbose_name= "Categoria"
        verbose_name_plural="Categorias"
        
    def __str__(self) -> str:
        return self.categoria_investigacion
    
class Investigacion(models.Model):
    
    #de muchos a muchos
    categorias_investigacion= models.ForeignKey(Categoria_Inv,on_delete=models.CASCADE, verbose_name='Categoria', null=True, blank=True)
    titulo=models.CharField(verbose_name="Titulo",max_length=150)
    resumen=models.TextField()
    imagen_d=models.ImageField(upload_to="Imagen Destacada",verbose_name="Subir una foto", null=True,blank=True)
    link = models.URLField(verbose_name = "Linkedin", null=True, blank= True)
    archivo = models.FileField(upload_to = "Uploaded Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    slug = models.SlugField(max_length=100, unique=True)

    class meta:
        verbose_name= "Investigacion"
        verbose_name_plural="Investigaciones"
        
    def __str__(self) -> str:
        return self.titulo
    
    def slug(self):
        return slugify(self.titulo)
    
class Persona(AbstractUser):
    TIPO_DOCUMENTO_CH=[
        ('cedula','Cedula'),
        ('pasaporte','Pasaporte')
    ]
    username=models.CharField(max_length=100, unique=True)
    email= models.EmailField(max_length=150, unique=True,blank=True,null=True,verbose_name="Correo")
    tipo_documento= models.CharField(verbose_name="Tipo de documento",max_length=20, choices=TIPO_DOCUMENTO_CH)
    cedula= models.CharField(verbose_name="Cedula",max_length=13,blank=True,null=True)
    first_name= models.CharField(verbose_name="Nombres",max_length=100,blank=True,null=True)
    last_name= models.CharField(verbose_name="Apellidos",max_length=100,blank=True,null=True)
    celular=models.CharField(verbose_name="N.Celular",max_length=13,blank=True,null=True)
    direccion=models.CharField(verbose_name="Direccion",max_length=20,blank=True,null=True)
    foto=models.ImageField(upload_to="Fotos_usuarios/",verbose_name="Subir una foto", null=True,blank=True)
    
    
    class meta:
        verbose_name= "Persona"
        verbose_name_plural="Personas"
    #metodo para presentar el objeto creado
    def __str__(self):
        return self.cedula+self.last_name+self.first_name
    
class Administrador(Persona):
    fecha_inicio=models.DateTimeField()
    fecha_actualizacion=models.DateTimeField()
    estado=models.BooleanField()
    class meta:
        verbose_name= "Administrador"
        verbose_name_plural="Administradores"
    def __str__(self):
            return self.cedula+self.last_name+self.first_name

class Estudio(models.Model):
    TIPO_ESTUDIO_CH=[
        ('primaria','Primaria'),
        ('secundaria','Secundaria'),
        ('tercer','Tercer')
    ]
    nombre_insti=models.CharField(verbose_name="Tipo de estudio ",max_length=100, choices=TIPO_ESTUDIO_CH)
    insti= models.CharField(verbose_name="Nombre Institución",max_length=100,blank=True,null=True)
    fecha_gra= models.DateField(blank=True,null=True,verbose_name="Fecha Graduación")
    fecha_reg= models.DateField(verbose_name="Fecha de Registro",blank=True,null=True)
    num_reg=models.CharField(verbose_name="Número de Registro",max_length=20,blank=True,null=True,unique=True)
    archivo = models.FileField(upload_to = "TituloPDF",blank=True,null=True)
    
    
    class meta:
        verbose_name= "Estudio"
        verbose_name_plural="Estudios"
    #metodo para presentar el objeto creado
    def __str__(self):
        return self.nombre_insti 
    
class Curso(models.Model):
    #de muchos a muchos
    TIPO_CERTIFICADO_CH=[
        ('asistencia','Asistencia'),
        ('aprobacion','Aprobacion')
    ]
    titulo=models.CharField(verbose_name="Titulo Curso",max_length=150)
    nombre= models.CharField(verbose_name="Nombre Organizador",max_length=100,blank=True,null=True)
    horas=models.CharField(verbose_name="Horas del Curso",max_length=3,blank=True,null=True)
    tipo_certificado= models.CharField(verbose_name="Tipo de Certificado",max_length=20, choices=TIPO_CERTIFICADO_CH)
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    class meta:
        verbose_name= "Curso"
        verbose_name_plural="Cursos"
    def __str__(self):
            return slugify(self.titulo) 
        
class Experiencia(models.Model):

    nombre_emp=models.CharField(verbose_name="Nombre Empresa",max_length=150)
    cargo= models.CharField(verbose_name="Cargor",max_length=100,blank=True,null=True)
    actividades=models.CharField(verbose_name="Actividades que realiza",max_length=400,blank=True,null=True)
    fecha_inicio_e=models.DateField()
    fecha_fin_e=models.DateField()
    class meta:
        verbose_name= "Experiencia"
        verbose_name_plural="Experiencias"
    def __str__(self):
            return slugify(self.nombre_emp)

""" class Hoja(Experiencia,Curso,Estudio):


    idiomas= models.CharField(verbose_name="Cargor",max_length=100,blank=True,null=True)
    afinidades=models.CharField(verbose_name="Actividades que realiza",max_length=400,blank=True,null=True,unique=True)
    class meta:
        verbose_name= "Experiencia"
        verbose_name_plural="Experiencias"
    def __str__(self):
            return self. """
        
class Autor(Persona):
    #de muchos a muchos
    estudios= models.ManyToManyField(Estudio, related_name="estudio",blank=True)
    cursos= models.ManyToManyField(Curso,related_name="curso", blank=True)
    experiencias= models.ManyToManyField(Experiencia,related_name="experiencia", blank=True)
    investigaciones= models.ManyToManyField(Investigacion,related_name="investigacion", blank=True)
    class meta:
        verbose_name= "Autor"
        verbose_name_plural="Autores"
    def __str__(self):
            return self.cedula 