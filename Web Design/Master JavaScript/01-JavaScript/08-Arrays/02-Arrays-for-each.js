var lenguajes = new Array("Php", "js", "go", "java");

document.write("<h1>Lenguajes</h1>");
document.write("<ul>");

// El primer parametro es el mimso elemento, ya no accedemos con []
// el segundo es el indice, si lo ocupamos (opcional)
// el tercero es el array mismo (opcional)
lenguajes.forEach((elemeto, indice) =>{
    document.write("<li>" + indice + " - " + elemeto + "</li>");
})
document.write("</ul>");