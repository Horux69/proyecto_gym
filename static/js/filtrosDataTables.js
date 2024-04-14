$(document).ready(function() {
    $("#sidebarCollapse").on('click', function() {
        $("#sidebar").toggleClass('active');
        adjustContentWidth(); // Llama a la función para ajustar el ancho del contenido
    });

    // Función para ajustar el ancho del contenido
    function adjustContentWidth() {
        if ($("#sidebar").hasClass('active')) {
            $("#content").addClass('active');
        } else {
            $("#content").removeClass('active');
        }
    }

    // Llama a la función cuando se carga la página por primera vez
    adjustContentWidth();
});