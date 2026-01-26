"""
Tarea: Implementación de Constructores y Destructores en Python
Nombre del Estudiante: MARIA ESTHEFANIA VELEZ FREIRE
Asignatura: Técnicas de Programación
"""

class Recurso:
    """
    Clase que simula el manejo de un recurso (por ejemplo, una conexión o archivo).
    Demuestra el uso de __init__ para abrir y __del__ para cerrar.
    """

    def __init__(self, nombre_recurso):
        """
        CONSTRUCTOR (__init__):
        Se ejecuta automáticamente al crear una instancia de la clase.
        Aquí inicializamos el estado del objeto.
        """
        self.nombre = nombre_recurso
        print(f"--> [Constructor] Inicializando recurso: '{self.nombre}'...")
        print(f"    (El recurso '{self.nombre}' está listo para usarse)")

    def usar_recurso(self):
        """Método simple para simular actividad."""
        print(f"    *** Trabajando con {self.nombre} ***")

    def __del__(self):
        """
        DESTRUCTOR (__del__):
        Se ejecuta automáticamente cuando el objeto es destruido por el
        recolector de basura de Python (al finalizar el programa o usar 'del').
        Aquí cerramos conexiones o liberamos memoria.
        """
        print(f"--> [Destructor] Liberando/Cerrando recurso: '{self.nombre}'.")
        print("    (Limpieza completada)")

# --- Ejecución del Programa ---
if __name__ == "__main__":
    # 1. Creamos el objeto (Se llama al constructor)
    mi_recurso = Recurso("Archivo_Datos.txt")

    # 2. Usamos el objeto
    mi_recurso.usar_recurso()

    # 3. El programa termina aquí.
    # Python detectará que el objeto ya no se usa y llamará al destructor automáticamente.
    print("--- Fin de la ejecución principal ---")