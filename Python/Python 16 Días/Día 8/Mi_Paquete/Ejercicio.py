"""
Un paquete es un directorio que contiene muchos modulos.
Este paquete tiene un modulo que puede quedar vacio __init__py.

Puede tener subpaquetes y cada subpaquete debe tener su init.

Para importar un subpaquete debe ir el nombre del paquete un punto y el nombre
del subpaquete.
"""
from Paquete_Ivan import suma_resta
from Paquete_Ivan.Sub_Paquete import Saludar

suma_resta.sumar(10, 10)
suma_resta.restar(10, 5)

Saludar.saludo()