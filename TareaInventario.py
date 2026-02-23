import os


class Producto:
    """Clase que representa un producto en el inventario."""

    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

    def a_texto(self):
        """Convierte los atributos del producto a una cadena de texto separada por comas."""
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}\n"


class Inventario:
    """Clase que maneja la colección de productos y las operaciones de archivo."""

    def __init__(self, archivo="inventario.txt"):
        self.productos = {}  # Usamos un diccionario para búsquedas rápidas por ID
        self.archivo = archivo
        # Intentar cargar los datos al momento de iniciar el programa
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Lee el archivo de texto y reconstruye el inventario."""
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:  # Ignorar líneas vacías
                        try:
                            # Desempaquetar los datos separados por coma
                            id_prod, nombre, cantidad, precio = linea.split(',')
                            self.productos[id_prod] = Producto(id_prod, nombre, int(cantidad), float(precio))
                        except ValueError:
                            # Captura errores si una línea del archivo está corrupta o mal formateada
                            print(f"⚠️ Advertencia: Línea corrupta ignorada en el archivo: {linea}")
            print(f"✅ Inventario cargado exitosamente desde '{self.archivo}'.")

        except FileNotFoundError:
            # Si el archivo no existe, lo notificamos y lo creamos vacío
            print(f"ℹ️ Archivo '{self.archivo}' no encontrado. Se creará uno nuevo automáticamente.")
            try:
                open(self.archivo, 'w').close()  # Crea el archivo vacío
            except Exception as e:
                print(f"❌ Error crítico al intentar crear el archivo: {e}")

        except PermissionError:
            # Captura errores si el programa no tiene permisos de lectura
            print(f"❌ Error: No tienes permisos para leer el archivo '{self.archivo}'.")

        except Exception as e:
            # Captura cualquier otro error inesperado
            print(f"❌ Error inesperado al cargar el archivo: {e}")

    def guardar_en_archivo(self):
        """Sobrescribe el archivo de texto con el inventario actual en memoria."""
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                for producto in self.productos.values():
                    f.write(producto.a_texto())
            print(f"💾 Cambios guardados exitosamente en '{self.archivo}'.")

        except PermissionError:
            print(f"❌ Error: No tienes permisos de escritura en el archivo '{self.archivo}'.")
        except Exception as e:
            print(f"❌ Error inesperado al guardar el archivo: {e}")

    def añadir_producto(self, producto):
        """Añade un producto a la memoria y guarda los cambios en el archivo."""
        if producto.id_producto in self.productos:
            print("❌ Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id_producto] = producto
            print(f"✅ Producto '{producto.nombre}' añadido a la memoria.")
            self.guardar_en_archivo()  # Actualizar el archivo inmediatamente

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza un producto existente y guarda los cambios en el archivo."""
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].cantidad = nueva_cantidad
            if nuevo_precio is not None:
                self.productos[id_producto].precio = nuevo_precio
            print("✅ Producto actualizado correctamente en la memoria.")
            self.guardar_en_archivo()  # Actualizar el archivo
        else:
            print("❌ Error: Producto no encontrado en el inventario.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto y refleja el cambio en el archivo."""
        if id_producto in self.productos:
            producto_eliminado = self.productos.pop(id_producto)
            print(f"✅ Producto '{producto_eliminado.nombre}' eliminado de la memoria.")
            self.guardar_en_archivo()  # Actualizar el archivo
        else:
            print("❌ Error: Producto no encontrado en el inventario.")

    def mostrar_inventario(self):
        """Imprime todos los productos actuales."""
        if not self.productos:
            print("📭 El inventario está vacío.")
        else:
            print("\n--- 📦 Inventario Actual ---")
            for producto in self.productos.values():
                print(producto)
            print("----------------------------\n")


def menu_principal():
    """Interfaz de usuario por consola."""
    # Al instanciar el inventario, automáticamente busca e intenta cargar el archivo
    inventario = Inventario()

    while True:
        print("\n=== 🛠️ Sistema de Gestión de Inventarios ===")
        print("1. Añadir nuevo producto")
        print("2. Actualizar producto existente")
        print("3. Eliminar producto")
        print("4. Mostrar todo el inventario")
        print("5. Salir del programa")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            print("\n-- Añadir Producto --")
            id_prod = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre: ")
            try:
                cant = int(input("Ingrese la cantidad (número entero): "))
                precio = float(input("Ingrese el precio (número decimal): "))
                nuevo_producto = Producto(id_prod, nombre, cant, precio)
                inventario.añadir_producto(nuevo_producto)
            except ValueError:
                print("❌ Error de formato: La cantidad debe ser un número entero y el precio un número válido.")

        elif opcion == '2':
            print("\n-- Actualizar Producto --")
            id_prod = input("Ingrese el ID del producto a actualizar: ")

            try:
                cant_input = input("Ingrese la nueva cantidad (presione Enter para omitir): ")
                cant = int(cant_input) if cant_input else None

                precio_input = input("Ingrese el nuevo precio (presione Enter para omitir): ")
                precio = float(precio_input) if precio_input else None

                if cant is not None or precio is not None:
                    inventario.actualizar_producto(id_prod, cant, precio)
                else:
                    print("ℹ️ No se realizaron cambios.")
            except ValueError:
                print("❌ Error de formato: Los valores numéricos no son válidos.")

        elif opcion == '3':
            print("\n-- Eliminar Producto --")
            id_prod = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_prod)

        elif opcion == '4':
            inventario.mostrar_inventario()

        elif opcion == '5':
            print("Saliendo del sistema... ¡Hasta luego! 👋")
            break

        else:
            print("❌ Opción no válida. Por favor, seleccione un número del 1 al 5.")


# Punto de entrada del script
if __name__ == "__main__":
    menu_principal()