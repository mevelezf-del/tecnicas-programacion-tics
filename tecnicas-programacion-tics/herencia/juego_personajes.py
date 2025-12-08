# juego_personajes.py
# Ejemplo de HERENCIA (y polimorfismo) en Python
# Autor: Tu Nombre - Técnicas de Programación

class Personaje:
    """
    Clase base que representa un personaje genérico.
    Contiene atributos y métodos comunes para cualquier tipo de personaje.
    """

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def mostrar_atributos(self):
        """Muestra en pantalla los atributos del personaje."""
        print(self.nombre, ":", sep="")
        print("· Fuerza:       ", self.fuerza)
        print("· Inteligencia: ", self.inteligencia)
        print("· Defensa:      ", self.defensa)
        print("· Vida:         ", self.vida)

    def esta_vivo(self):
        """Devuelve True si el personaje tiene vida mayor a 0."""
        return self.vida > 0

    def morir(self):
        """Establece la vida en 0 e informa que el personaje ha muerto."""
        self.vida = 0
        print(self.nombre, "ha muerto.")

    def calcular_daño(self, enemigo):
        """
        Cálculo genérico de daño.
        Las clases hijas pueden redefinir este método (polimorfismo).
        """
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        """Realiza un ataque contra otro personaje."""
        daño = self.calcular_daño(enemigo)
        if daño < 0:
            daño = 0

        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)

        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, ":", enemigo.vida)
        else:
            enemigo.morir()


class Guerrero(Personaje):
    """
    Clase Guerrero que hereda de Personaje.
    Agrega el atributo espada e implementa su propio cálculo de daño.
    """

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, poder_espada):
        # Llamamos al constructor de la clase base
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.poder_espada = poder_espada

    def mostrar_atributos(self):
        """Muestra los atributos del guerrero, incluyendo su espada."""
        super().mostrar_atributos()
        print("· Poder de espada:", self.poder_espada)

    def calcular_daño(self, enemigo):
        """
        Cálculo de daño específico para el Guerrero.
        Usa la fuerza multiplicada por el poder de la espada.
        """
        return self.fuerza * self.poder_espada - enemigo.defensa


class Mago(Personaje):
    """
    Clase Mago que hereda de Personaje.
    Agrega el atributo libro e implementa su propio cálculo de daño.
    """

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, poder_hechizo):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.poder_hechizo = poder_hechizo

    def mostrar_atributos(self):
        """Muestra los atributos del mago, incluyendo su libro de hechizos."""
        super().mostrar_atributos()
        print("· Poder de hechizo:", self.poder_hechizo)

    def calcular_daño(self, enemigo):
        """
        Cálculo de daño específico para el Mago.
        Usa la inteligencia multiplicada por el poder del hechizo.
        """
        return self.inteligencia * self.poder_hechizo - enemigo.defensa


def combate(jugador_1, jugador_2):
    """
    Función que simula un combate por turnos entre dos personajes.
    """
    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\n====================== Turno", turno, "======================")
        print(">>> Acción de", jugador_1.nombre)
        jugador_1.atacar(jugador_2)

        if not jugador_2.esta_vivo():
            break  # Si el segundo muere, termina el combate

        print(">>> Acción de", jugador_2.nombre)
        jugador_2.atacar(jugador_1)
        turno += 1

    print("\n==================== Fin del combate ====================")
    if jugador_1.esta_vivo() and not jugador_2.esta_vivo():
        print("Ha ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo() and not jugador_1.esta_vivo():
        print("Ha ganado", jugador_2.nombre)
    elif not jugador_1.esta_vivo() and not jugador_2.esta_vivo():
        print("Ambos han muerto. Empate.")
    else:
        print("El combate ha terminado sin ganador claro.")


if __name__ == "__main__":
    # Creamos un guerrero y un mago para probar el ejemplo
    guerrero = Guerrero("Guts", 20, 8, 5, 100, poder_espada=4)
    mago = Mago("Vanessa", 6, 18, 3, 100, poder_hechizo=3)

    print("=== Atributos iniciales ===")
    guerrero.mostrar_atributos()
    print()
    mago.mostrar_atributos()

    # Iniciamos el combate (aquí puedes sacar tu captura de pantalla)
    combate(guerrero, mago)
