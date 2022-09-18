# STRING
"""
Los String son un tipo de dato formado por cadenas o secuancias de caracteres. Para determinar
un string hacemos uso de comillas dobles o simples, para indicar donde comienza y termina
dicho string.

Dentro de un String pueden ir numeros, caracteres especiales, etc. Siempre que este
entre comillas sera tratado como texto.

- CONCATENACION
Se usa para unificar cadenas de texto en una sola.

- CARACTERES ESPECIALES
Indicamos que un caracterer es especial con la barra invertida '\'.
De este modo al imprimirlo Python realizara acciones como aplicar sangria,
incluir comillas.
"""

print("100 + 2")  # Esto es un string, no una operacion. Mostrara la expresion literal.

# Concatenacion
print("Hola Ivan")
print("Hola" + "Ivan")  # Concatenar dos string
print("Hola " + "Ivan")  # Agregar espacio primera forma
print("Hola" + " Ivan")  # Agregar espacio segunda forma
print("Hola" + " " + "Ivan")  # Agregar espacio FORMA RECOMENDADA

# Ejemplo concatencion con varaibles
nombre = "Ivan"
saludo = "Como estas"
print(saludo + nombre)
print(saludo + " " + nombre)

# Caracteres Especiales
print("Mi nombre es \"Ivan\"")  # FORMA RECOMENDADA para imprimir comillas
print('This isn\'t a number')
print("Mi nombre es \nIvan")  # Hace un salto de linea
print("\tMi nombre es Ivan")  # Hace una tabluacion
print("Esta es una barra invertida: \\")  # Muestra la barra invertida

