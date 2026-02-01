import os
import subprocess

# Tarea: Adaptación de Dashboard para gestión de tareas
# Estudiante: [TU NOMBRE AQUÍ]
# Descripción: Script adaptado para navegar por las tareas de POO.

def mostrar_codigo(ruta_script):
    """
    Muestra el contenido de un archivo antes de ejecutarlo.
    """
    ruta_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
            print(f"\n----------------------------------\n")
    except FileNotFoundError:
        print("El archivo no se encontró.")

def ejecutar_codigo(ruta_script):
    """
    Ejecuta el script de Python seleccionado.
    """
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['python', ruta_script], shell=True)
        else:  # Linux / macOS
            subprocess.Popen(['python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_menu():
    """
    Menú principal dinámico.
    """
    ruta_base = os.path.dirname(__file__)

    # --- ZONA DE CONFIGURACIÓN ---
    # Aquí puedes agregar o quitar tareas según necesites.
    # Asegúrate de que las carpetas (UNIDAD 1, etc.) existan en tu proyecto.
    opciones = {
        "1": "UNIDAD 1/1.2. Tecnicas de Programacion/1.2-1. Ejemplo Tecnicas de Programacion.py",
        "2": "UNIDAD 1/1.2. Tecnicas de Programacion/1.2-2. Ejemplo Abstraccion.py",
        "3": "UNIDAD 1/1.2. Tecnicas de Programacion/1.2-3. Ejemplo Encapsulamiento.py",
        "4": "UNIDAD 2/2.1. Constructores y Destructores/2.1-1. Constructores.py"
        # Puedes agregar mas lineas siguiendo el formato: "Numero": "Ruta/Del/Archivo.py"
    }
    # -----------------------------

    while True:
        print("\n******** Menu Principal - Dashboard POO ********")
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige una opción: ")

        if eleccion == '0':
            print("Saliendo del programa...")
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            
            print(f"\nSeleccionaste: {opciones[eleccion]}")
            accion = input("¿Qué deseas hacer? (1: Ejecutar, 2: Ver código, 3: Volver): ")
            
            if accion == '1':
                ejecutar_codigo(ruta_script)
            elif accion == '2':
                mostrar_codigo(ruta_script)
            elif accion == '3':
                continue
            else:
                print("Opción no válida.")
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()

