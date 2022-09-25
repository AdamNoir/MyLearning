# EXERCISE 2
"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña 
introducida por el usuario 
coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

password = input("Crea una Contraseña una contraseña: ")

password_conf = input("Intrega tu contraseña: ")

if password.lower() == password_conf.lower():
    print(f"La contraseña es: {password}")
else:
    print("Las contraseñas no Coinicen.")