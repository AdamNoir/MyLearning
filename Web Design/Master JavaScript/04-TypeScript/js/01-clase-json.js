console.log("Clase Json.js")

var bicicleta = {
    color: "Rojo",
    modelo: "BMX",
    frenos: "De disco",
    velocidadMaxima: "6okm",
    // Metodos
    cambiaColor: function(nuevo_color){
        // bicicleta.color = nuevo_color;
        this.color = nuevo_color;
    }
};

console.log(bicicleta);