from django.urls import path
from .views import home, formulario, mascotas, listar_mascotas,eliminar_mascotas,modificar_mascota



urlpatterns = [
    path('', home, name="home"),
    path('formulario/', formulario, name="formulario"),
    path('mascotas/', mascotas, name="mascotas"),
    path('listar-mascotas/', listar_mascotas, name="listado_mascotas"),
    path('eliminar-mascotas/<id>/', eliminar_mascotas, name="eliminar_mascotas"),
    path('modificar-mascotas/<id>/', modificar_mascota, name="modificar_mascota"),
]
