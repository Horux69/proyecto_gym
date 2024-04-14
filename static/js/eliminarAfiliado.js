$(document).ready(function() {
    $(document).on('click', '.delete-afiliado', function(e) {
        // capturamos el evento clic del boton eliminar sede
        var afiliadoID = $(this).data('id');
        //capturamos el id de la sede en una variable
        deleteAfiliado(afiliadoID);
        //enviamos el id a la funcion sededelete
        e.preventDefault();
    });
});
function deleteAfiliado(id_afiliado) {
    swal({
        title: '\u00bfEstas seguro?',
        text: "El afiliado se desactivar\u00e1 de forma permanente!",
        icon: 'warning',
        buttons: true,
        dangerMode: true,
        allowOutsideClick: false
    }).then((willDelete) => {
        if (willDelete) {
            $.ajax({
                type: 'get',
                url: '/afiliados/desactivarAfiliado/' + id_afiliado,
            }).done(function(respuesta) {
                if (respuesta == false) {
                    swal("Error", "Un error ha ocurrido!", {
                        icon: "error",
                    });
                    location.reload();
                } else {
                    swal("Confirmaci\u00f3n", "El afiliado ha sido desactivado!", {
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