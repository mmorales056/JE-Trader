function formulario_alumno(ruta){
    $.ajax({
        url: ruta,
        success:function(rpta){
            $('#config_alumno').html(rpta);
        },
        error: function(){
            console.log('error');
        }
    })
}


function calcular_top(cantidad){

}

function form_edit_alumno(ruta) {
    $.ajax({
        url: ruta,
        success:function(rpta){
            $('#config_alumno').html(rpta);
        },
        error: function(){
            console.log('error');
        }
    })

    
}



var date = new Date();
var now = date.getUTCFullYear()+"-"+(date.getMonth()+1)+"-"+date.getDate();
let actual = moment(now)

$(document).ready(function() {
    $('.alumnos').DataTable({

        "language": {
                        "sProcessing": "Procesando...",
                        "sLengthMenu": "Mostrar _MENU_ registros",
                        "sZeroRecords": "No se encontraron resultados",
                        "sEmptyTable": "Ningún dato disponible en esta tabla =(",
                        "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
                        "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
                        "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
                        "sInfoPostFix": "",
                        "sSearch": "Buscar:",
                        "sUrl": "",
                        "sInfoThousands": ",",
                        "sLoadingRecords": "Cargando...",
                        "oPaginate": {
                            "sFirst": "Primero",
                            "sLast": "Último",
                            "sNext": "Siguiente",
                            "sPrevious": "Anterior"
                        },
                        "oAria": {
                            "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
                            "sSortDescending": ": Activar para ordenar la columna de manera descendente"
                        },
                        "buttons": {
                            "copy": "Copiar",
                            "colvis": "Visibilidad"
                        },                    
                    },
        rowCallback:function(row,data){
            let fin = moment(data[4]);
            let diff = (fin.diff(actual,'days'))
            let d = Number(diff);
            console.log(d);
            if (d <= 3) {
                $($(row).find('td')[1]).css("background-color","#E60026", "color","white");                
                $($(row).find('td')[1]).css("color","white");
                $($(row).find('td')[2]).css("background-color","#E60026", "color","white")
                $($(row).find('td')[2]).css("color","white")
                $($(row).find('td')[3]).css("background-color","#E60026", "color","white")
                $($(row).find('td')[3]).css("color","white")
                $($(row).find('td')[4]).css("background-color","#E60026", "color","white")
                $($(row).find('td')[4]).css("color","white")
                $($(row).find('td')[7]).removeClass("d-none")

                //
            }            
        }

        
    });
  });

  function renovar(ruta) {
    $('#modal_alumno').modal('show');
    $('#renovar').click(function() {
        if( $('#meses').val() > 0 ){
            let csrftoken = getCookie('csrftoken');
            $.ajax({
                url: ruta,
                data:{
                    'meses':$('#meses').val(),
                    'estado': 'si',
                    csrfmiddlewaretoken: csrftoken,
                },
                method: 'POST',
                success:function(respuesta) {          
                    
                    alert('Alumno Renovado');
                    location.reload()
                    
                }
              });
        }else{
            alert('Necesita Numero de Meses')
        }
        
      });

      
  }



  function form_renovar_alumno(ruta){
      $.ajax({
          url:ruta,
          success: function (respuesta) {
              $('#config_alumno').html(respuesta);
          },
          error: function () {
              console.log('Error')
          }
      })
  }



function eliminar(ruta) {
    $('#modal_eliminar').modal('show');
    $('#eliminar').click(function() {
            $.ajax({
                url: ruta,
                success:function(respuesta) {          
                    
                    location.reload()
                }
              });                
      });
    
}

  //MEtodo para tomar e crf_token de las coockies de django
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    //RETORNANDO EL TOKEN
    return cookieValue;
}
