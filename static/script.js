function entradas(){
   if (document.getElementById('salida').checked){
      document.getElementById('pesticidas').style.display= "inherit";
      document.getElementById('fertilizantes').style.display= "none";
   } else{
      document.getElementById('pesticidas').style.display= "none";
      document.getElementById('fertilizantes').style.display= "inherit";

   }

}

function editar(action, id) {
    if (action === 'entrar') {
        // Ocultar todas las cards
        let cards = document.getElementsByClassName('card');
        document.getElementById('footer_parcela').style.display = 'none';
        for (let i = 0; i < cards.length; i++) {
            cards[i].style.display = 'none';
        }
        // Mostrar el formulario de edición correspondiente
        document.getElementById('editar_parcela_' + id).style.display = 'block';
    } else if (action === 'salir') {
        // Ocultar el formulario de edición
        document.getElementById('editar_parcela_' + id).style.display = 'none';
        // Mostrar todas las cards
        let cards = document.getElementsByClassName('card');
        for (let i = 0; i < cards.length; i++) {
            cards[i].style.display = 'block';
        }
    } else if (action === 'entrar_inventario'){
        //ocultar la tabla
        console.log(id);
        let cards = document.getElementsByClassName('main_table');
        for (let i = 0; i < cards.length; i++) {
            cards[i].style.display = 'none';
        }
        document.getElementById('editar_parcela_' + id).style.display = 'block';
    } else if (action === 'salir_inventario') {
        // Ocultar el formulario de edición
        document.getElementById('editar_parcela_' + id).style.display = 'none';
        // Mostrar todas las cards
        let cards = document.getElementsByClassName('main_table');
        for (let i = 0; i < cards.length; i++) {
            cards[i].style.display = 'block';
        }
    }
}

function tarea(action) {
    var tratar = document.getElementById('tratar');
    var labores = document.getElementById('labores');
    var fertilizar = document.getElementById('fertilizar');

    if (action === "fitosanitarios") {
        labores.style.display = "none";
        tratar.style.display = "inherit";
        fertilizar.style.display = "none";
    } else if (action === "culturales") {
        labores.style.display = "inherit";
        tratar.style.display = "none";
        fertilizar.style.display = "none";
    } else if (action === "fertilizacion") {
        labores.style.display = "none";
        tratar.style.display = "none";
        fertilizar.style.display = "inherit";
    } else {
        labores.style.display = "none";
        tratar.style.display = "none";
        fertilizar.style.display = "none";
    }
}

function form_view() {
    if (document.getElementsByClassName("main")[0]){
        document.getElementsByClassName("main")[0].style.display = "none";

    }
    let cards = document.getElementsByClassName('main_table');
        for (let i = 0; i < cards.length; i++) {
            cards[i].style.display = 'none';
        }
    let mostrar = document.getElementById("main_form");
    mostrar.style.display = "block";
    

}

window.onload = function () {
    const botones = document.querySelectorAll(".boton_status");

    botones.forEach((boton) => {
        const id = boton.getAttribute("data-id");

        // Verifica si ya fue marcado como culminado
        if (localStorage.getItem("tarea_culminada_" + id) === "true") {
            boton.textContent = "Culminado";
            boton.disabled = true;
            boton.style.backgroundColor = "gray";
        }

        // Evento para actualizar el estado
        boton.addEventListener("click", function () {
            boton.textContent = "Culminado";
            boton.disabled = true;
            boton.style.backgroundColor = "gray";

            // Guardar en localStorage
            localStorage.setItem("tarea_culminada_" + id, "true");
        });
    });
};