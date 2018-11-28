from django.urls import path
from .views import listar_mascotas,agregar_mascotas,eliminar_mascotas,modificar_mascota

urlpatterns = [
    path('listar-mascotas/', listar_mascotas, name="api_listar_mascotas"),
    path('agregar-mascotas/', agregar_mascotas, name="api_agregar_mascotas"),
    path('eliminar-mascotas/<id>/', eliminar_mascotas, name="api_eliminar_mascotas"),
    path('modificar-mascotas/<id>/', modificar_mascota, name="api_modificar_mascota"),
]