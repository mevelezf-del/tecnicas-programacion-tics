# cuenta_bancaria.py
# Ejemplo de ENCAPSULACIÓN en Python
# Autor: Tu Nombre - Técnicas de Programación

class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria sencilla.
    Se usa ENCAPSULACIÓN para proteger el saldo mediante
    un atributo privado (__saldo) y métodos de acceso.
    """

    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular          # atributo público
        self.__saldo = saldo_inicial    # atributo privado (encapsulado)

    def depositar(self, monto):
        """Aumenta el saldo solo si el monto es válido."""
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso de ${monto:.2f}")
        else:
            print("El monto a depositar debe ser mayor que cero.")

    def retirar(self, monto):
        """Disminuye el saldo solo si hay fondos suficientes."""
        if monto <= 0:
            print("El monto a retirar debe ser mayor que cero.")
        elif monto > self.__saldo:
            print("Fondos insuficientes. No se puede realizar el retiro.")
        else:
            self.__saldo -= monto
            print(f"Retiro exitoso de ${monto:.2f}")

    def obtener_saldo(self):
        """
        Devuelve el saldo actual.
        Este método es la única forma de leer el saldo desde fuera.
        """
        return self.__saldo

    def mostrar_informacion(self):
        """Muestra el titular y el saldo de la cuenta."""
        print("=== Información de la cuenta ===")
        print("Titular:", self.titular)
        print(f"Saldo actual: ${self.__saldo:.2f}")
        print("================================")


if __name__ == "__main__":
    # Ejemplo de uso de la clase (para tu captura de pantalla)

    # Crear una cuenta a nombre del estudiante TIC
    cuenta = CuentaBancaria("Estudiante TIC", saldo_inicial=100.0)

    # Mostrar información inicial
    cuenta.mostrar_informacion()

    # Realizar un depósito
    cuenta.depositar(50)

    # Intentar retirar un monto válido
    cuenta.retirar(30)

    # Intentar retirar más de lo que hay en la cuenta
    cuenta.retirar(500)

    # Consultar el saldo final
    print("\nSaldo final en la cuenta:", cuenta.obtener_saldo())
