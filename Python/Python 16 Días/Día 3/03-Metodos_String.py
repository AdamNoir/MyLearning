# METODOS STRINGS
"""
- upper(): Pasa un texto a mayusculas
- lower(): Pasa un texto a minusculas
- split(): Sepra en un texto en partes (Listas)
- join(): Une textos usando un separador
- Find(): Encuentra un Substring
- replace(): remplaza un substring
"""

# Mayusculas y Minusculas
my_text = "Este es el String de Ivan"
print(my_text.upper())
print(my_text.lower())
# Puede funcionar usando solo un indice o substring
print(my_text[2:6].upper())

# Split separa EN BASE A LO ESPACIOS EN BLANCO y almacena en una lista
print(my_text.split())
# Podemos pasar un seaparor personalizado
print(my_text.split("e"))

# Join Unir
a = "Hola"
b = "Como"
c = "Estan"
d = "Todos"
# Pasamos entre los parentesis una lista,
# Establecemos el String QUE SERA EL CARACTER QUE UNA A LOS DEMAS STRING
union = ".".join([a, b, c, d])
print(union)

# Find funciona igual que index, PERO CUANDO NO ENCUENTRA UN CARACTER DA -1 EN VEZ DE EXCEPCION
print(my_text.find("x"))
print(my_text.find("I"))

# Replace remplaza un substring por otro
# Ocupa saber LO QUE VAMOS A REMPLZAR, Y EL PORQUE LO VAMOS A REMPLAZAR
print(my_text.replace("Ivan", "Amigos"))
print(my_text.replace("e", "*"))
