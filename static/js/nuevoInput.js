function mostrarCampoOculto() {

    let padre = document.getElementById('caja_otro_campo');

    let nuevo_campo = document.createElement("input");

    nuevo_campo.setAttribute('type', "text");
    nuevo_campo.setAttribute('name', "otro_perfil");
    nuevo_campo.setAttribute('id', "otro_perfil");
    nuevo_campo.setAttribute('class', "inputText");
    nuevo_campo.setAttribute('pattern', "[A-Za-z]{4,16}");
    nuevo_campo.setAttribute('title', "Has ingresado algo diferente a letras.");
    nuevo_campo.setAttribute('maxlenght', "200");
    nuevo_campo.setAttribute('minlenght', "1");
    nuevo_campo.setAttribute('required', "true");
    nuevo_campo.setAttribute('placeholder', "Escribe la o las leciones que tiene")

    padre.appendChild(nuevo_campo);

}


document.addEventListener("DOMContentLoaded", () =>{
    
    let perfil = document.getElementById('leciones');
    console.log(perfil)

    perfil.addEventListener("change", (campo) => { //change es el evento cambio, no se debe usar para tipo text, number, tel, etc, sirve para los select y files

        if (campo.target.value === "si") {

            mostrarCampoOculto();

        }else {

            if (document.getElementById('otro_perfil')) {

                document.getElementById('caja_otro_campo').removeChild(document.getElementById('otro_perfil'));

            }

        }


    });

});