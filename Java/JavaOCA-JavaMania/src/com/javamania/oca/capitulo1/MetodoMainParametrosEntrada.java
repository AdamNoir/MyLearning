package com.javamania.oca.capitulo1;

/*Que imprime esta  clase cuando ejecutamos los siguentes comandos:
*
* java MetodoMainParametrosEntrada hola mundo
* java MetodoMainParametrosEntrada MetodoMainParametrosEntrada hola mundo
* java MetodoMainParametrosEntrada
* java MetodoMainParametrosEntrada java true public
* java MetodoMainParametrosEntrada null            null           null
* java MetodoMainParametrosEntrada "Hola Hola Mundo"
* java MetodoMainParametrosEntrada "Hola" "Hola" "Java"
* */
public class MetodoMainParametrosEntrada {
    public static void main(String[]args){
        System.out.println(args[0]);
        System.out.println(args[1]);
        System.out.println(args[2]);

        // Revisar si es nullo o no el arreglo args
        boolean isNull = args == null;
        boolean isEmpy = args.length == 0;

        System.out.println(isNull);
        System.out.println(isEmpy);
    }
}
