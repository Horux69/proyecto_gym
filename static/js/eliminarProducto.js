$(document).ready(function() {
    $(document).on('click', '.delete-producto', function(e) {
        // capturamos el evento clic del boton eliminar sede
        var productoID = $(this).data('id');
        //capturamos el id de la sede en una variable
        deleteProducto(productoID);
        //enviamos el id a la funcion sededelete
        e.preventDefault();
    });
});
function deleteProducto(id_producto) {
    swal({
        title: '\u00bfEstas seguro?',
        text: "El producto se desactivar\u00e1 de forma permanente!",
        icon: 'warning',
        buttons: true,
        dangerMode: true,
        allowOutsideClick: false
    }).then((willDelete) => {
        if (willDelete) {
            $.ajax({
                type: 'get',
                url: '/inventario/desactivar/' + id_producto,
            }).done(function(respuesta) {
                if (respuesta == false) {
                    swal("Error", "Un error ha ocurrido!", {
                        icon: "error",
                    });
                    location.reload();
                } else {
                    swal("Confirmaci\u00f3n", "El producto ha sido desactivada!", {
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