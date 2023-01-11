interface CamisetaBase{
    setColor(color);
    getColor();
}

// Decorar
function estampar(logo: string){
    return function(target: Function){
        target.prototype.estampacion = function():void{
            console.log("Camiseta estampada con el logo de: " + logo)
        }
    }
}

// clase
// export es para poder usarla desde otro
@estampar("Gucci")
class Camiseta1 implements CamisetaBase{
    // Propiedades
    private color: string;
    private modelo: string;
    private marca: string;
    private talla: string;
    private precio: number;

    // Constructor
    constructor(color, modelo, marca, talla, precio){
        this.color = color;
        this.modelo = modelo;
        this.marca = marca;
        this.talla = talla;
        this.precio = precio;
    }

    // Metodos
    public setColor(color){
        this.color = color;
    }

    public getColor(){
        return this.color;
    }
}

// Herencia
class Sudadera extends Camiseta{
    public capucha: boolean;

    setCapucha(capucha: boolean){
        this.capucha = capucha;
    }

    getCapucha():boolean{
        return this.capucha;
    }
}


var camiseta = new Camiseta("rojo", "modelo", "marca", "talla", 12);
console.log(camiseta);
camiseta.setColor("red");
camiseta.estampacion();
console.log(camiseta.getColor());

var capucha = new Sudadera("rojo", "modelo", "marca", "talla", 12);
capucha.setCapucha(true);
console.log(capucha);