public class VarArgs {
    public static void main(String[] args) {
        // Llamar función con VarArgs
        System.out.println(sumar(10, 102, 312, 5, 1, 5, 1, 3));
        // Llamar función con varios parametros
        sumarSaludo("Ivan", 23, 1, 2, 3, 4, 5, 6, 7, 8, 9);
    }

    // Definir función de sumar n cantidad de numeros
    public static int sumar(int... numeros){
        int suma = 0;
        for(int numero : numeros){
            suma = suma + numero;
        }
        return suma;
    }

    // Varios parámetros y Varargs
    public static void sumarSaludo(String nombre, int edad, int... numeros){
        int suma = 0;
        for(int numero : numeros){
            suma = suma + numero;
        }
        System.out.println("La suma de " + nombre + " de edad " + edad + " es: " + suma);
    }
}
