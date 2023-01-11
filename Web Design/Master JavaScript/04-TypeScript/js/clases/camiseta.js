// clase
// export es para poder usarla desde otro
var Camiseta = /** @class */ (function () {
    // Constructor
    function Camiseta(color, modelo, marca, talla, precio) {
        this.color = color;
        this.modelo = modelo;
        this.marca = marca;
        this.talla = talla;
        this.precio = precio;
    }
    // Metodos
    Camiseta.prototype.setColor = function (color) {
        this.color = color;
    };
    Camiseta.prototype.getColor = function () {
        return this.color;
    };
    return Camiseta;
}());
/*
var camiseta = new Camiseta("rojo", "modelo", "marca", "talla", 12);
console.log(camiseta);
camiseta.setColor("red");
console.log(camiseta.getColor());
*/ 
