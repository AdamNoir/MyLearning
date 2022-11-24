public class FuncionMetodos {
    public static void main(String[]args){
        // Llamar funcion
        saludar("Nombre");

        // Llamar Metodo
        FuncionMetodos funcionMetodos = new FuncionMetodos();
        funcionMetodos.myMetodo("Hola");
    }

    // Definir funcion
    public static void saludar(String nombre){
        System.out.println("Hola " + nombre + " desde funcion.");
    }

    // Definir Un metodo
    public void myMetodo(String saludo){
        System.out.println(saludo + " desde Metodo.");
    }
}
