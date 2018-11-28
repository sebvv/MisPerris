from django.shortcuts import render,redirect
from .models import Comuna, Region, Formulario, Mascotas , Vivienda,  Estado, Genero, Raza
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required




def home(request):
    return render(request, 'core/index.html')

def formulario(request):
    comuna = Comuna.objects.all()
    region = Region.objects.all()
    vivienda = Vivienda.objects.all()
    #enviamos las marcas hacia el templates 
    variables ={
        'comuna':comuna,
        'region':region,
        'vivienda':vivienda,
    }

    #preguntaremos si es post   
    if request.POST:
        #si la peticion es post obtendremos los datos
        formu = Formulario()
        formu.rut_postulante = request.POST.get('txtRut')
        formu.nombre_postulante = request.POST.get('txtNombre')
        formu.fecha_nacimiento = request.POST.get('txtFechaNacimiento')
        formu.correo = request.POST.get('txtCorreo')
        formu.telefono = request.POST.get('txtNumero')
        #la marca es una colaboracion de clases 
        #por lo tanto para obtener el combo primero
        #crearemos un objeto marca
        region = Region()
        region.id = request.POST.get('cboRegion')
        formu.region = region

        comuna= Comuna()
        comuna.id = request.POST.get('cboComuna')
        formu.comuna = comuna

        vivienda= Vivienda()
        vivienda.id = request.POST.get('cboVivienda')
        formu.vivienda = vivienda

        #procedemos a guardar el auto en la BBDD
        try: 
            formu.save()
            variables['mensaje'] = "Guardado Correctamente"
        except:
            variables['mensaje'] = "No se ha podido Guardar"           

    return render(request, 'core/formulario.html',variables)

#CRUD  mascotas  
@login_required       
def mascotas(request):
    genero = Genero.objects.all()
    estado = Estado.objects.all()
    raza = Raza.objects.all()
    #enviamos las marcas hacia el templates 
    variables ={
        'genero':genero,
        'estado':estado,
        'raza':raza

    }
    if request.POST:

        mascota = Mascotas()
        mascota.nombre_mascota = request.POST.get('txtNombre')  
        mascota.fecha_ingreso = request.POST.get('txtFechaIngreso')
        mascota.fecha_nacimiento = request.POST.get('txtFechaNacimiento')
        mascota.foto =  request.FILES.get('imagen')

        genero= Genero()
        genero.id = request.POST.get('cboGenero')
        mascota.genero = genero

        raza= Raza()
        raza.id = request.POST.get('cboRaza')
        mascota.raza = raza

        estado= Estado()
        estado.id = request.POST.get('cboEstado')
        mascota.estado = estado

        try: 
            mascota.save()
            variables['mensaje'] = "Guardado Correctamente"
        except:
            variables['mensaje'] = "No se ha podido Guardar"   

    return render(request, 'core/mascotas.html',variables)
@login_required 
def listar_mascotas(request):

    mascota = Mascotas.objects.all()


    return render(request, 'core/listar_mascotas.html',{ 
        'mascota':mascota 
    })

def eliminar_mascotas(request,id):

    mascota = Mascotas.objects.get(id=id)

    try:
        mascota.delete()
        mensaje = "Eliminado Correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido Eliminar"
        messages.error(request, mensaje)

    return redirect('listado_mascotas')

def modificar_mascota(request,id):

    mascota = Mascotas.objects.get(id=id)
    genero = Genero.objects.all()
    estado = Estado.objects.all()
    raza = Raza.objects.all()
    #enviamos las marcas hacia el templates 
    variables ={
        'mascota':mascota,
        'genero':genero,
        'estado':estado,
        'raza':raza

    }
    if request.POST:

        mascota = Mascotas()
        mascota.id = request.POST.get('txtId')
        mascota.nombre_mascota = request.POST.get('txtNombre')  
        mascota.fecha_ingreso = request.POST.get('txtFechaIngreso')
        mascota.fecha_nacimiento = request.POST.get('txtFechaNacimiento')


        genero= Genero()
        genero.id = request.POST.get('cboGenero')
        mascota.genero = genero

        raza= Raza()
        raza.id = request.POST.get('cboRaza')
        mascota.raza = raza

        estado= Estado()
        estado.id = request.POST.get('cboEstado')
        mascota.estado = estado

        try: 
            mascota.save()
            messages.success(request,'Modificado correctamente')
        except:
            messages.error(request,'No se ha podido Modificar')
        return redirect('listado_mascotas')

    return render(request, 'core/modificar.html', variables)