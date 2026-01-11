# -----------------------------------------------------------------------------
# Nombre: calculo_notas.py
# Descripción: Calcula el promedio de un alumno y determina si aprobó.
# -----------------------------------------------------------------------------

def realizar_calculo():
    # --- Entrada de datos ---
    nombre_alumno = input("Ingresa el nombre del alumno: ")
    cantidad_clases = 3
    print(f"Ingresa las notas de las {cantidad_clases} clases:")
    nota_1 = float(input("Nota 1: "))
    nota_2 = float(input("Nota 2: "))
    nota_3 = float(input("Nota 3: "))

    # --- Procesamiento ---
    promedio_final = (nota_1 + nota_2 + nota_3) / cantidad_clases
    estado_aprobado = promedio_final >= 7.0

    # --- Salida ---
    print(f"\nAlumno: {nombre_alumno}")
    print(f"Promedio: {promedio_final:.2f}")
    print(f"¿Aprobado?: {estado_aprobado}")

if __name__ == '__main__':
    realizar_calculo()