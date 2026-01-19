# Tarea: Aplicación de Conceptos de POO en Python
# Definición de Clase, Herencia, Encapsulamiento y Polimorfismo

# 1. DEFINICIÓN DE CLASE BASE (Abstracción)
class Empleado:
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.id_empleado = id_empleado
        # 2. ENCAPSULAMIENTO
        # El salario base es privado (__), no se puede acceder directamente desde fuera.
        self.__salario_base = 0

    # Método público para establecer salario (Setter con validación)
    def establecer_salario(self, monto):
        if monto > 0:
            self.__salario_base = monto
            print(f"Salario base de {self.nombre} actualizado.")
        else:
            print("El salario debe ser positivo.")

    # Método público para obtener salario (Getter)
    def obtener_salario(self):
        return self.__salario_base

    # 3. POLIMORFISMO (Método base que será sobrescrito)
    def calcular_pago(self):
        # Por defecto retorna el salario base
        return self.__salario_base

    def describir_rol(self):
        return "Empleado general"


# 4. HERENCIA (Clase Derivada 1)
class Gerente(Empleado):
    def __init__(self, nombre, id_empleado, bono):
        # Uso de super() para llamar al constructor de la clase padre
        super().__init__(nombre, id_empleado)
        self.bono = bono

    # 5. POLIMORFISMO (Sobreescritura de método)
    # El gerente calcula su pago diferente (salario + bono)
    def calcular_pago(self):
        # Accedemos al salario base mediante el getter público
        return self.obtener_salario() + self.bono

    def describir_rol(self):
        return "Gerente de Departamento"


# HERENCIA (Clase Derivada 2)
class Desarrollador(Empleado):
    def __init__(self, nombre, id_empleado, horas_extra):
        super().__init__(nombre, id_empleado)
        self.horas_extra = horas_extra
        self.pago_por_hora = 20  # Tarifa fija por hora extra

    # POLIMORFISMO
    def calcular_pago(self):
        return self.obtener_salario() + (self.horas_extra * self.pago_por_hora)

    def describir_rol(self):
        return "Desarrollador de Software"


# --- EJECUCIÓN DEL PROGRAMA ---
if __name__ == "__main__":
    print("=== SISTEMA DE GESTIÓN DE EMPLEADOS ===")

    # DEFINICIÓN DE OBJETOS (Instancias)
    empleado1 = Gerente("Carlos Pérez", "G001", 500)
    empleado2 = Desarrollador("Ana López", "D005", 10)

    # Demostración de Encapsulamiento
    print("\n--- Configuración de Salarios (Encapsulamiento) ---")
    empleado1.establecer_salario(3000)
    empleado2.establecer_salario(2000)

    # Intento de acceso directo (esto daría error si se descomenta)
    # print(empleado1.__salario_base)

    # Demostración de Polimorfismo
    print("\n--- Cálculo de Pagos (Polimorfismo) ---")

    personal = [empleado1, empleado2]

    for p in personal:
        # El mismo método 'calcular_pago' actúa diferente según la clase
        pago_total = p.calcular_pago()
        print(f"Empleado: {p.nombre} | Rol: {p.describir_rol()} | Total a pagar: ${pago_total}")