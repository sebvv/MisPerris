from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest
#el serializer permite transformar un arreglo en un json 
from django.core import serializers
import json
from core.models import Mascotas ,  Estado, Genero, Raza
# Create your views here.
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

def listar_mascotas(request):
    mascota = Mascotas.objects.all()

    mascotaJson = serializers.serialize('json', mascota)
    
    return HttpResponse(mascotaJson, content_type="application/json ")
#
@csrf_exempt
@require_http_methods(['POST'])     
def agregar_mascotas(request):
    body = request.body.decode('utf-8')
    bodyDict = json.loads(body)

    mascota = Mascotas()
    mascota.nombre_mascota = bodyDict['txtNombre']
    mascota.fecha_ingreso = bodyDict['txtFechaIngreso']
    mascota.fecha_nacimiento = bodyDict['txtFechaNacimiento']
    mascota.genero = Genero(id=bodyDict['genero_id'])
    mascota.raza = Raza(id=bodyDict['raza_id'])
    mascota.estado = Estado(id=bodyDict['estado_id'])
    
    try: 
        mascota.save()
        return HttpResponse(json.dumps({'mensaje':'Guardado correctamente'}), content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha podido guardar'}), content_type="application/json")
        
    
@csrf_exempt
@require_http_methods(['DELETE'])     
def eliminar_mascotas(request,id):

    mascota = Mascotas.objects.get(id=id)

    try:
        mascota.delete()
        return HttpResponse(json.dumps({'mensaje':'Eliminado correctamente'}), content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha podido Eliminar'}), content_type="application/json")

@csrf_exempt
@require_http_methods(['PUT'])  
def modificar_mascota(request,id):

    body = request.body.decode('utf-8')
    bodyDict = json.loads(body)
    mascota = Mascotas.objects.get(id=bodyDict["id"]) 
    mascota.nombre_mascota = bodyDict['txtNombre']
    mascota.fecha_ingreso = bodyDict['txtFechaIngreso']
    mascota.fecha_nacimiento = bodyDict['txtFechaNacimiento']
    mascota.genero = Genero(id=bodyDict['genero_id'])
    mascota.raza = Raza(id=bodyDict['raza_id'])
    mascota.estado = Estado(id=bodyDict['estado_id'])

    try: 
        mascota.save()
        return HttpResponse(json.dumps({'mensaje':'Modificado correctamente'}), content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha podido Modificar'}), content_type="application/json")
        