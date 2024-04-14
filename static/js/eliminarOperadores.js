$(document).ready(function() {
    $(document).on('click', '.delete-operador', function(e) {
        // capturamos el evento clic del boton eliminar sede
        console.log('hola');
        var operadorID = $(this).data('id');
        //capturamos el id de la sede en una variable
        deleteOperador(operadorID);
        //enviamos el id a la funcion sededelete
        e.preventDefault();
    });
});
function deleteOperador(id_operador) {
    swal({
        title: '\u00bfEstas seguro?',
        text: "El operador se desactivar\u00e1 de forma permanente!",
        icon: 'warning',
        buttons: true,
        dangerMode: true,
        allowOutsideClick: false
    }).then((willDelete) => {
        if (willDelete) {
            $.ajax({
                type: 'get',
                url: '/operadores/desactivar/' + id_operador,
            }).done(function(respuesta) {
                if (respuesta == false) {
                    swal("Error", "Un error ha ocurrido!", {
                        icon: "error",
                    });
                    location.reload();
                } else {
                    swal("Confirmaci\u00f3n", "El operador ha sido desactivado!", {
                        icon: "success",
                    });
                    setTimeout(() => {
                        location.reload();
                    }, 1000);
                }
            });
        }
    });
}