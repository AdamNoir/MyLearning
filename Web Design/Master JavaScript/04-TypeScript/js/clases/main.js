"use strict";
exports.__esModule = true;
var camiseta_1 = require("./camiseta");
var Main = /** @class */ (function () {
    function Main() {
        console.log("Aplicacion JS");
    }
    Main.prototype.getCamiseta = function () {
        return new camiseta_1.Camiseta("Rojo", "ASDAS", "ASDASDASD", "ASDASD", 100);
    };
    return Main;
}());
var main = new Main();
