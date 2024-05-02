$(document).ready(function() {
    $(document).on('click', '.delete-membresia', function(e) {
        // capturamos el evento clic del boton eliminar sede
        var membresiaID = $(this).data('id');
        //capturamos el id de la sede en una variable
        deleteMembresia(membresiaID);
        //enviamos el id a la funcion sededelete
        e.preventDefault();
    });
});
function deleteMembresia(id_membresia) {
    swal({
        title: '\u00bfEstas seguro?',
        text: "La membresia se desactivar\u00e1 de forma permanente!",
        icon: 'warning',
        buttons: true,
        dangerMode: true,
        allowOutsideClick: false
    }).then((willDelete) => {
        if (willDelete) {
            $.ajax({
                type: 'get',
                url: '/membresias/desactivarMembresia/' + id_membresia,
            }).done(function(respuesta) {
                if (respuesta == false) {
                    swal("Error", "Un error ha ocurrido!", {
                        icon: "error",
                    });
                    location.reload();
                } else {
                    swal("Confirmaci\u00f3n", "La membresia ha sido desactivada!", {
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