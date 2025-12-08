# figuras.py
# Ejemplo de ABSTRACCIÓN en Python
# Autor: Tu Nombre - Técnicas de Programación

from abc import ABC, abstractmethod

class Figura(ABC):
    """
    Clase abstracta que representa una figura geométrica.
    Define la interfaz común para todas las figuras (método area).
    """

    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def area(self):
        """Método abstracto que calculará el área de la figura."""
        pass

    def mostrar_area(self):
        """Muestra el área de la figura en pantalla."""
        print(f"El área de la figura {self.nombre} es: {self.area():.2f}")


class Rectangulo(Figura):
    """
    Clase concreta que representa un rectángulo.
    Implementa el cálculo de área específico para un rectángulo.
    """

    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Circulo(Figura):
    """
    Clase concreta que representa un círculo.
    Implementa el cálculo de área específico para un círculo.
    """

    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def area(self):
        PI = 3.14159
        return PI * (self.radio ** 2)


class Triangulo(Figura):
    """
    Clase concreta que representa un triángulo.
    Implementa el cálculo de área específico para un triángulo.
    """

    def __init__(self, base, altura):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


if __name__ == "__main__":
    # Ejemplo de uso (para tu captura de pantalla)

    rect = Rectangulo(base=5, altura=3)
    circ = Circulo(radio=4)
    tri = Triangulo(base=6, altura=2)

    print("=== Ejemplo de abstracción con figuras geométricas ===\n")

    rect.mostrar_area()
    circ.mostrar_area()
    tri.mostrar_area()
