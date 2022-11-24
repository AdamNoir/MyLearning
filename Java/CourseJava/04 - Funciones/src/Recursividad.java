public class Recursividad {
    public static void main(String[]args){
        cuentaRegresiva(10);
        System.out.println(factorial(5));
    }

    // Función de cuenta regresiva
    public static void cuentaRegresiva(int numero){
        numero --;
        if (numero > 0){
            System.out.println(numero);
            // Llamar a la misma funcion
            cuentaRegresiva(numero);
        }else {
            System.out.println("La cuenta a terminado. 0");
        }
    }

    // Función Factorial
    public static int factorial(int numero){
        if (numero > 1){
            numero = numero * factorial(numero - 1);
        }
        return numero;
    }
}
