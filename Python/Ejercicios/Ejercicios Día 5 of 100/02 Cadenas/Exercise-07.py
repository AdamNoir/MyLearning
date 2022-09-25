# EXERCISE 7
"""
Pedir al usuario un correo electronico, cambiar dominio despues del arroba por ceu.es
"""
email = input("Ingresa un Email: ")
#arroba = email.find("@")
print(email[:email.find("@") + 1] + "ceu.es")
