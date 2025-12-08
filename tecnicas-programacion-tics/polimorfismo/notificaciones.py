# notificaciones.py
# Ejemplo de POLIMORFISMO en Python
# Autor: Tu Nombre - Técnicas de Programación

from abc import ABC, abstractmethod

class Notificacion(ABC):
    """
    Clase base abstracta que representa una notificación genérica.
    Define la interfaz (método enviar) que deben implementar las clases hijas.
    """

    def __init__(self, mensaje):
        self.mensaje = mensaje

    @abstractmethod
    def enviar(self):
        """Método abstracto que será implementado por cada tipo de notificación."""
        pass


class NotificacionEmail(Notificacion):
    """
    Clase que representa una notificación enviada por correo electrónico.
    Hereda de Notificacion e implementa su propia forma de enviar().
    """

    def __init__(self, destinatario_email, mensaje):
        super().__init__(mensaje)
        self.destinatario_email = destinatario_email

    def enviar(self):
        """Implementación específica de envío por Email."""
        print("=== Enviando EMAIL ===")
        print("Para   :", self.destinatario_email)
        print("Mensaje:", self.mensaje)
        print("======================\n")


class NotificacionSMS(Notificacion):
    """
    Clase que representa una notificación enviada por SMS.
    Hereda de Notificacion e implementa su propia forma de enviar().
    """

    def __init__(self, numero_celular, mensaje):
        super().__init__(mensaje)
        self.numero_celular = numero_celular

    def enviar(self):
        """Implementación específica de envío por SMS."""
        print("=== Enviando SMS ===")
        print("Número :", self.numero_celular)
        print("Mensaje:", self.mensaje)
        print("====================\n")


def enviar_notificacion(notificacion):
    """
    Función que recibe un objeto de cualquier clase que herede de Notificacion
    y llama al método enviar(). Aquí se ve el polimorfismo:
    distintas clases, mismo método.
    """
    notificacion.enviar()


if __name__ == "__main__":
    # Creamos dos tipos de notificaciones distintas
    email = NotificacionEmail(
        destinatario_email="estudiante.tic@correo.com",
        mensaje="Tu tarea de Técnicas de Programación fue subida a GitHub."
    )

    sms = NotificacionSMS(
        numero_celular="+593999999999",
        mensaje="Recuerda entregar el PDF de la tarea en Moodle."
    )

    # Lista de notificaciones (todas se tratan igual)
    lista_notificaciones = [email, sms]

    print("=== Ejemplo de polimorfismo con notificaciones ===\n")
    for n in lista_notificaciones:
        # No importa si es Email o SMS, todas tienen enviar()
        enviar_notificacion(n)
