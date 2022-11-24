public class SobreCarga {
    public static void main(String[]args){
        // Llamar a la función con tipo de retorno int
        System.out.println(sumar(10, 10));

        // Llamar función con tipo de retorno double
        System.out.println(sumar(10.0, 11.65));
    }

    // definir función sumar con tipo de retorno int
    public static int sumar(int numero1, int numero2){
        return numero1 + numero2;
    }

    // definir función sumar con tipo de retorno double
    public static double sumar(double numero1, double numero2){
        return numero1 + numero2;
    }
}
