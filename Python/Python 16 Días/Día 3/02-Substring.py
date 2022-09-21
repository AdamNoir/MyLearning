# EXTRAER SUBSTRINGS
"""
Podemos extrarer porciones de un texto usando el slicing (rebanar, cortar)
Esta extracion podemos almacenarla en una variable para usarla despues.
    - Primero indicamos desde que caracter queremos cortar
    - Despues incluimos hasta donde queremos cortar (sin incluir este valor, n-1)
    - Y un tercer factor nos dice de cuantos en cuantos caracteres queremos cortar
Esto se establece entre corcheres y separados por dos puntos.
"""
my_text = "ABCDEGHIJKLMNÑOPKR"
# Tomara desde el indice 2 hasta 8-1
sub_string = my_text[2:8]
print(sub_string)

# Si no incluirmos valor al final, solo dos puntos lo hara hasta el FINAL DE LA CADENA
# Lo mismo pasa si no colocamos inicio y establecemos Fin, lo hara DESDE EL PRINCIPIO DE LA CADENA
sub_string = my_text[:8]
print(sub_string)
sub_string = my_text[3:]
print(sub_string)

# Agregando un tercer valor tomara caracteres saltando en el numero establecido
sub_string = my_text[1:8:2]
print(sub_string)

# Podemos solo incluir este valor para que vaya saltando toda la cadena
sub_string = my_text[::3]
print(sub_string)

# Si solo agregamos el "Invervalo" en negativo obtendremos LA CADENA AL REVEZ
sub_string = my_text[::-1]
print(sub_string)

# Ira salteando pero a la inversa
sub_string = my_text[::-3]
print(sub_string)