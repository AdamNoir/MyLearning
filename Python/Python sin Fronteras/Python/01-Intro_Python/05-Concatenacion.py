# CONCATENACIÓN

"""La concatenacion es unir varias cadenas de caracteres (Strings) para formar una oracion.
Eso se usa mas que nada para obtener mensajes mucho mas claros para el usuarios."""

nombre = "Ivan"
apellido = "Gutierrez"
edad = 24

# Para concatenar usamos + entre variables
print("Tu nombre es: " + nombre + " y tu apellido es: " + apellido + " Y tu edad es: " + str(edad))
# Al ser edad un int, usamos la funcion de str para convertirlo a String y poderlo concatenar.

# No solo podemos concatenar en un print, podemos hacerlo para formar nuevas variables
nombre_completo = nombre + " " + apellido
print("Tu nombre completo es: " + nombre_completo)
