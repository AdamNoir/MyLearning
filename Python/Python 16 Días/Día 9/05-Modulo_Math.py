# MODULO MATH
"""
Contiene un conjunto de metodos y constantes que se usan para resolver tareas 
matematicas con cierto grado de complejidad.

- Relaciones trigonometricas:  seno, coseno, tangenta, inversas e hiperbolicas
- Funciones Logaritmicas
- Potencias y Raices
- Combinatoria y permutaciones
- Redondeos
- Factoriales

Constantes: 
- Pi
- e o Constante de Euler
- Tau
- Infinito
- Nulo
"""

import math

# Redondeo hacia abajo
resultado = math.floor(98.678)
print(resultado)

# Redondear hacia arriba
resultado = math.ceil(98.678)
print(resultado)

numero_pi = math.pi
print(numero_pi)

# Logaritmo
# En funcion a una base nos dice a que valor debemos exponer
# un numero para llegar a dicha base
logaritmo = math.log(1000, 10)
print(logaritmo)

# Tangente
tangente = math.tan(2565)
print(tangente)

# Coseno
coseno = math.cos(2565)
print(coseno)

# Factorial de un numero
factorial = math.factorial(7)
print(factorial)