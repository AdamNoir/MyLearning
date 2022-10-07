# EXERCISE 10
tipo = input("Ingresa el tipo de pizza: VEGETARIANA / NO VEGETARIANA")
ingrediente = ""
if tipo.lower() == "vegetariana":
    print("ELIGE UN INGRDIENTE: ")
    print("1) Primiento")
    print("2) Tofu")
    ingrediente = input("Ingresar ingrediente:")
elif tipo.lower() == "no vegetariana":
    print("ELIGE UN INGRDIENTE: ")
    print("1) Peperoni")
    print("2) Jamon")
    print("3) Salon")
    ingrediente = input("Ingresar ingrediente:")
else:
    print("TIPO DE PIZA NO ENCONTRADO")
print(f"El tipo de piza es {tipo} y los ingredientes son {ingrediente}")