# PROYECTO
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        cliente_str = f"Cliente: {self.nombre} {self.apellido}+" \
               f"Numero de Cuenta: {self.numero_cuenta}+" \
               f"Balance: {self.balance}"
        return cliente_str

    def depositar(self, cantidad):
        self.balance = self.balance + cantidad

    def retirar(self, cantidad):
        if self.balance >= cantidad:
            self.balance -= cantidad
            print("Retiro Realizado")
        else:
            print("Sin fondos")


def inicio(cliente):
    print("-" * 40)
    while True:
        print("""
        [1] Despositar a la Cuenta
        [2] Retirar de la Cuenta
        [3] Salir""")
        eleccion = int(input("Elige opcion: "))
        if eleccion == 1:
            cantidad = int(input("Ingresa cuanto quieres depositar: "))
            cliente.depositar(cantidad)
            print(cliente)
        elif eleccion == 2:
            cantidad = int(input("Ingresa cuanto quieres Retirar: "))
            cliente.retirar(cantidad)
            print(cliente)
        elif eleccion == 3:
            print("Gracias por su Visita.")
            break


cliente1 = Cliente("Ivan", "Ibarra", 10000, 0)
inicio(cliente1)
