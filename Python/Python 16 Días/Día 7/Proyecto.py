# PROYECTO
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super(Persona, self).__init__(nombre, apellido)
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
            self.balance = self.balance - cantidad
        else:
            return f"No tienes fondos."


"""def crear_cliente():
    nombre = input("Ingrea un nombre: ")
    apellido = input("Ingreas un apellido ")
    numero_cuenta = int(input("Ingrea un numero de cuenta(Solo numeros): "))
    balance = int(input("Ingresa un balance: "))
    cliente = Cliente(nombre, apellido, numero_cuenta, balance)
    print("Cliente creado: ")
    print(cliente)
    return cliente
"""

def inicio(cliente):
    print("-" * 40)
    while True:
        eleccion = int(input("Elige opcion: "))
        if eleccion == 1:
            cantidad = int(input("Ingresa cuanto quieres depositar: "))
            cliente.depositar(cantidad)
            print(cliente)
        elif eleccion == 2:
            cantidad = int(input("Ingresa cuanto quieres depositar: "))
            cliente.retirar(cantidad)
            print(cliente)
        elif eleccion == 3:
            break


cliente1 = Cliente("Ivan", "Ibarra", 10000, 10)
inicio(cliente1)
