# EXERCISE 12
"""
Una barra de pan cuesta 3.49, al pan que no es del dia se le resta el 60%.
Mostrar en una linea el precio original, el descuento y el total
"""
total_pan = int(input("Ingresa el total de pan: "))
descuento = 0.6
precio = 3.49
print(f"Una barra cuesta: {precio}, el cuesto es: {descuento * 100} y el total es: {round((total_pan * precio) * (1 - descuento), 2)}")
