# ==========================================
# Clase Producto
# ==========================================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Usamos un guion bajo para denotar que son atributos "privados" (Encapsulamiento)
        self._id_producto = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # --- Getters (Métodos para obtener los valores) ---
    def get_id(self):
        return self._id_producto

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # --- Setters (Métodos para actualizar los valores) ---
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    # Método para representar el objeto como texto fácilmente
    def __str__(self):
        return f"ID: {self._id_producto} | Nombre: {self._nombre} | Cant: {self._cantidad} | Precio: ${self._precio:.2f}"


# ==========================================
# Clase Inventario
# ==========================================
class Inventario:
    def __init__(self):
        # La estructura de datos es una lista de objetos Producto
        self.productos = []

    def añadir_producto(self, producto):
        # Validar que el ID sea único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return  # Salimos del método sin añadir

        self.productos.append(producto)
        print("¡Producto añadido exitosamente!")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("¡Producto eliminado exitosamente!")
                return
        print("Error: No se encontró ningún producto con ese ID.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("¡Producto actualizado exitosamente!")
                return
        print("Error: No se encontró ningún producto con ese ID.")

    def buscar_producto(self, nombre):
        # Comprensión de lista para buscar coincidencias (ignorando mayúsculas/minúsculas)
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

        if resultados:
            print("\n--- Resultados de la búsqueda ---")
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario Completo ---")
            for p in self.productos:
                print(p)


# ==========================================
# Interfaz de Usuario en la Consola (Menú)
# ==========================================
def menu():
    inventario = Inventario()

    while True:
        print("\n" + "=" * 30)
        print(" SISTEMA DE GESTIÓN DE INVENTARIOS ")
        print("=" * 30)
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            try:
                id_prod = input("Ingrese el ID del producto: ")
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))

                nuevo_producto = Producto(id_prod, nombre, cantidad, precio)
                inventario.añadir_producto(nuevo_producto)
            except ValueError:
                print("Error: La cantidad debe ser un número entero y el precio un número decimal.")

        elif opcion == '2':
            id_prod = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_prod)

        elif opcion == '3':
            id_prod = input("Ingrese el ID del producto a actualizar: ")
            print("Deje en blanco si no desea actualizar el campo.")
            str_cantidad = input("Nueva cantidad: ")
            str_precio = input("Nuevo precio: ")

            # Procesamos las entradas para ver si el usuario escribió algo
            cantidad = int(str_cantidad) if str_cantidad.strip() else None
            precio = float(str_precio) if str_precio.strip() else None

            if cantidad is not None or precio is not None:
                inventario.actualizar_producto(id_prod, cantidad, precio)
            else:
                print("No se realizaron cambios.")

        elif opcion == '4':
            nombre = input("Ingrese el nombre (o parte del nombre) a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_todos()

        elif opcion == '6':
            print("Saliendo del sistema... ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu()