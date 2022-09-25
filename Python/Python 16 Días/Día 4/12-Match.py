# MATCH (SWTICH CASE)
"""
FUNCION SOLO DISPOBLE DESDE PYTHON 3.10

Se le conoce coincidencia de patrones. Permit asociar acciones espesificar basadas en las formas
o patrones de tipos de datos.

Es como tener un monton de if anidados. La ventaja es que consume menos memoria.
"""

# Ejemplo IF
serie = "N-02"

if serie == "N-01":
    print("SAMSUNG")
elif serie == "N-02":
    print("NOKIA")
elif serie == "N-03":
    print("MOTOROLA")
else:
    print("No se que celular sea")

# Ejemplo Match
match serie:
    case "N-01":
        print("SAMSUNG")
    case "N-02":
        print("NOKIA")
    case "N-03":
        print("MOTOROLA")
    case _:
        print("No se que es eso")

# No solo queda en una opcion a lo if anidados, sino que tambien puede reconocer patrones
cliente = {"nombre": "Ivan",
           "edad": 24,
           "ocupacion": "Existir"}
pelicula = {"titulo": "Annie Hall",
            "ficha_tecnica": {
                "protagonista": "Daiane Keaton",
                "director": "Woody Allen"}}
elementos = [cliente, pelicula, "string"]

for elemento in elementos:
    match elemento:
        case {"nombre": nombre,
           "edad": edad,
           "ocupacion": ocupacion}:
            print("Es un cliente")
        case {"titulo": titulo,
            "ficha_tecnica": {
                "protagonista": protagonista,
                "director": director}}:
                print("Es una pelicula")
        case _:
            print("Sabe")
