public class Retorno {
    public static void main(String[]args){
        // Llamar a funcion y almacenar en una variable para imprimir
        String miSaludo = saludar("Ivan");
        System.out.println(miSaludo);

        // Llamar a funcion y almacenar en una variable para imprimir
        int resultadoSuma = sumar(1, 20);
        System.out.println(resultadoSuma);
    }

    // Definir función con tipo de retorno int
    public static int sumar(int numero1, int numero2){

        // Palabra clave que devuelve el valor. Explicitamente o cun una variable.
        return numero1 + numero2;
    }

    // Definir función con tipo de retorno String
    public static String saludar(String nombre){
        String saludo = "Hola, mucho gusto en conocerte " + nombre;
        return saludo;
    }
}
