# DATETIME
"""
Trabaja con fechas y horas, asi como con intervalos y duraciones.

- fechas: año, mes y dia. Los valores que recibe son integers y son rangos de fechas
"REALES". Pomdemos acceder a los atributos o partes de una fecha individualmente.
- hora: si no se indica nada el valor sera 0. Trabaja en formado de 24 horas.
Datos reales, hora, minutos, segundos y hasta microsegundos.
- fecha y hora: año, mes, dia, hora, minuo, microsegundo.
"""

import datetime
from datetime import datetime
from datetime import date

# Hora
"""mi_hora = datetime.time(17, 35, 10)
print(type(mi_hora))
print(mi_hora)
print(mi_hora.hour)"""

# Fecha
"""mi_fecha = datetime.date(2022, 10, 29)
print(mi_fecha)
print(mi_fecha.year)
print(mi_fecha.ctime())

# Fecha
print(mi_fecha.today())"""

# Fecha y hora
mi_fecha_hora = datetime(2025, 5, 12, 22, 10, 15, 2500)

# Remplazar valores de una fecha y hora.
mi_fecha_hora = mi_fecha_hora.replace(year=2035)
print(mi_fecha_hora)

# Diferencias de Dias entre dos Fechas
nacimiento = date(1995, 3, 5)
defuncion = date(2095, 6, 19)

# No muestra tiempo porque no se establecio.
vida = defuncion - nacimiento
print(vida)
print(vida.days)

# Diferencia de tiempo entre dos fechas y horas
despierto = datetime(2022, 11, 3, 7, 30)
duerme = datetime(2022, 11, 3, 23, 45)

tiempo_despierto = duerme - despierto
print(tiempo_despierto)
print(tiempo_despierto.seconds)

# Obtener fecha y hora actual
ahora = datetime.now()
print(ahora)