$(document).ready(function(){
    $("#formu").validate({
        rules:{
            txtRut:{
                required:true,
                minlength:9,
                maxlength:10
            },
            txtNombre:{
                required:true,
                minlength:3,
                maxlength:50
            },
            
            txtNumero:{
                required:true,
                number:true,
                minlength:8,
                maxlength:9
            },
            txtCorreo:{
                required: true,
                minlength:3,
                maxlength:50
            },
            cboRegion:{
                required:true
            },
            cboComuna:{
                required:true
            },
            txtFechaNacimiento:{
                required:true,
            },
            txtNombre:{
                required:true,
                minlength:3,
                maxlength:50
            },
            cboRaza:{
                required:true
            },
            txtFechaNacimiento:{
                required:true,
            },
            txtFechaIngreso:{
                required:true,
            },
            cboGenero:{
                required:true
            },
            cboEstado:{
                required:true
            }
        },
        messages:{
            txtRut:{
                required:"Este campo es requerido",
                number:"Debe ser numerico",
                minlength:"Minimo 9 dijitos",
                maxlength:"Maximo 10 dijitos"
            },
            txtNombre:{
                required:"Este campo es requerido",
                minlength:"Minimo 3 letras",
                maxlength:"Maximo 50 letras"
            },
            txtCorreo:{
                required:"Este campo es requerido",
                minlength:"Largo Minimo de 15 letras",
                max:"largo Maximo de 50 letras"
            },
            txtNumero:{
                required:"Este campo es requerido",
                number:"Debe ser numerico",
                minlength:"Minimo 8 dijitos",
                maxlength:"Maximo 9 dijitos"
            },
            cboRegion:{
                required:"Seleccione un opcion"
            },
            cboComuna:{
                required:"Seleccione un opcion"
            },
            txtFechaNacimiento:{
                required:"Este campo es requerido",
            },
            txtFechaIngreso:{
                required:"Este campo es requerido",
            },
            cboRaza:{
                required:"Seleccione un opcion"
            },
            cboGenero:{
                required:"Seleccione un opcion"
            },
            cboEstado:{
                required:"Seleccione un opcion"
            }
        }
    });
    });
    