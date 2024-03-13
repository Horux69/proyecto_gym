
// Función para validar los datos en tiempo real
function validarDatosEnTiempoReal() {
    // Obtener los valores desde el formulario
    var precio_compra = parseFloat(document.getElementById("precio_compra").value);
    var precio_venta = parseFloat(document.getElementById("precio_venta").value);
    var cantidad = parseInt(document.getElementById("cantidad").value);

    // Validar los datos
    if (precio_venta > precio_compra  && cantidad > 0) {
        document.getElementById("mensajeValidacion").innerText = "Los datos son válidos.";
    } else {
        document.getElementById("mensajeValidacion").innerText = "Los datos no son válidos. Por favor, revise.";
    }
}

// Asignar eventos input a los campos del formulario para activar la validación en tiempo real
document.getElementById("precio_compra").addEventListener("input", validarDatosEnTiempoReal);
document.getElementById("precio_venta").addEventListener("input", validarDatosEnTiempoReal);
document.getElementById("cantidad").addEventListener("input", validarDatosEnTiempoReal);