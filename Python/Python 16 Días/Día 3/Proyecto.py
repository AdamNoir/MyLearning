# PROYECTO - ANALIZADOR DE TEXTOS
"""
- Pida al usuario escribir un texto
- Pida tres letras
DEVOLVER:
    - Cuantas veces aparece cada letras
    - Contar todas las palabras -
    - Informar primera y ultima letra
    - Orden Inverso de las palabras -
    - Preguntar si existe Python -
"""
text = input("Ingresa un Texto: ")
text = text.lower()
letter1 = input("Ingresa una letra: ")
letter2 = input("Ingresa una letra: ")
letter3 = input("Ingresa una letra: ")

print(f"La letra {letter1} aparece un total de {text.count(letter1)} veces, {letter2} aparece {text.count(letter2)}, y {letter3} aparece {text.count(letter3)} veces")

# Contar todas las palabras
list_text = text.split()
print(f"El total de palabras en el texto es: {len(list_text)}")

# Informar primera y ultima letra
print(f"La primera letra del texto es: {text[0]} y la ultima letra del texto es: {text[len(text) - 1]}")

# Orden Inverso de las palabras
print(f"La cadena inversa es: {text[::-1]}")

# Preguntar si existe Python
is_python = "python" in text
print(f"¿Python se encuentra en el texto?: {is_python}")
