from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect
import json

# Create your views here.

#programamos primero el acceso al framewokr a traves del restapi
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

#importamos los datos del archivo serializers
from .serializers import InvestigacionSerializers, AdministradorSerializers, AutorSerializers

#importar el modelo
from.models import Autor, Investigacion, Persona, Administrador, Categoria_Inv,Curso,Estudio,Experiencia
from django.views import View
#formas creando directamente encampsularlos
#1metodo
class Index(View):
    def get(self, request):
        categorias = Categoria_Inv.objects.all() # seria de agg categorias 
        print(categorias)
        return render(request, 'presentacion/index.html', {'categorias' : categorias})

# ================== clase para mostrar los investigaciones de manera individual ¡¡¡¡
# listar investigaciones
class ListarInvestigaciones(View):
    def get(self, request):
        investigaciones = Investigacion.objects.all().order_by('categorias_investigacion')
        return render(request, 'investigacion/lista_inves.html', {'investigaciones': investigaciones })
class ListarAutores(View):
    def get(self, request):
       autores = Autor.objects.all().order_by('first_name')
        
       return render(request, 'autor/lista_inves.html', {'autores': autores })

# listar investigaciones tics
class ListarInvestigacionestics(View):
    def get(self, request, id_categoria):
        if not id_categoria:
            id_categoria=1
        investigar = Investigacion.objects.all().filter(categorias_investigacion=id_categoria)
        print(investigar)
        return render(request, 'tics/lista_inves.html', {'investigar': investigar})

# ver la investigacion
class VerInvestigacion(View):
    def get(self, request, id_investigacion):
        investigacion = Investigacion.objects.all().filter(id=id_investigacion)
        autores = Autor.objects.all().filter(autor__id=id_investigacion)
        #form = ReservaFormulario()
        investigacion=investigacion
        return render(request, 'investigacion/investigacion.html', {
            #'form': form,
            'investigacion': investigacion,
            'autores': autores 
        })

# ver el autor
class VerAutor(View):
    def get(self, request, id_autor):
        autor = Autor.objects.all().filter(id=id_autor)
        cursos = Curso.objects.all().filter(curso__id=id_autor)
        estudios = Estudio.objects.all().filter(estudio__id=id_autor)
        experiencias = Experiencia.objects.all().filter(experiencia__id=id_autor)
        print(cursos)
        #form = ReservaFormulario()
        autor=autor
        #print(form)
        return render(request, 'autor/autor.html', {
            #'form': form,
            'autor': autor,'cursos': cursos,
            'estudios': estudios, 'experiencias':experiencias
        })


class Investigacion_APIView(APIView):
    #metodo get para que puedan obtener la informacion
    def get(self, request, format=None, *args, **Kwargs):
        #realizar la consulta mediante el ORM de django para objeter todos las investigaciones
        investigaciones= Investigacion.objects.all()
        #utilizar la clase que habilital apra crear el ai y enviar las investigaciones registrados
        serializer= InvestigacionSerializers(investigaciones, many=True)
        # responde la data de los invetigaciones
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer= InvestigacionSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
class Investigacion_APIView_Detalles(View):
    #vamos a obtener todos los objetos
    def get_objeto(self, investigacion_id):
        try:
            return Investigacion.objects.get(id=investigacion_id)
        except Investigacion.DoesNotExist:
            raise Http404
    
    def  get(self, request, id_investigacion, format=None):
        investigacion= self.get_objeto(id_investigacion)
        serializer= InvestigacionSerializers(investigacion)
        return Response(serializer.data)
    
    #vamos a crear un metodo put
    
    def put(self, request, id_investigacion, format=None):
        investigacion= self.get_objeto(id_investigacion)
        serializer= InvestigacionSerializers(investigacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Autor_APIView(APIView):
    #metodo get para que puedan obtener la informacion
    def get(self, request, format=None, *args, **Kwargs):
        #realizar la consulta mediante el ORM de django para objeter todos los autores
#.........Ojo revisar aqui va Investigacion en vez de autor para revisar en caso de que salga error estar al pendiente ........
        autores= Autor.objects.all()
        #utilizar la clase que habilital apra crear el ai y enviar los emprendimientos registrados
        serializer= AutorSerializers(autores, many=True)
        # responde la data de las investigaciones
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer= AutorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)



class Autor_APIView_Detalles(View):
    #vamos a obtener todos los objetos
    def get_objeto(self, autor_id):
        try:
            return Autor.objects.get(id=autor_id)
        except Autor.DoesNotExist:
            raise Http404
    
    def  get(self, request, autor_id, format=None):
        autores= self.get_objeto(autor_id)
        serializer= AutorSerializers(autor_id)
        return Response(serializer.data)
    
    #vamos a crear un metodo put
    
    def put(self, request, autor_id, format=None):
        autores= self.get_objeto(autor_id)
        serializer= AutorSerializers(autores, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
