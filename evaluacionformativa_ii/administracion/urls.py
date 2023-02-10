from django.urls import path
from .import  views
from .views import*

app_name= 'administracion'


urlpatterns = [
    path('index', Index.as_view(), name="index"),
    # grupo de paths para las investigaciones
    path('investigaciones/listado',ListarInvestigaciones.as_view(),name='listado_investigaciones' ),
    path('autores/listado',ListarAutores.as_view(),name='listado_autores' ),
    path('investigaciones/listado/<int:id_categoria>',ListarInvestigacionestics.as_view(),name='listado' ),
    path('autores/autor/<int:id_autor>',VerAutor.as_view(),name='ver_autor' ),
    path('investigaciones/investigacion/<int:id_investigacion>',VerInvestigacion.as_view(),name='ver_investigacion' ),
    path("api/investigaciones", Investigacion_APIView.as_view(),name='lista_investigaciones'),
    path("api/investigaciones/<int:id_investigacion>", Investigacion_APIView_Detalles.as_view(),name='detalle_investigacion'),
    path("api/autores", Autor_APIView.as_view(),name='lista_autores'),
    path("api/autores/<int:id_autor>", Autor_APIView_Detalles.as_view(),name='detalle_autor'),
   
]