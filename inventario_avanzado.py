import json
import os


# ==========================================
# CLASE PRODUCTO
# ==========================================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Usamos encapsulamiento (atributos privados con __)
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters (para obtener los valores)
    def get_id(self):
        return self.__id_producto

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters (para modificar los valores)
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    # Método para convertir el objeto a un diccionario (facilita guardarlo en JSON)
    def to_dict(self):
        return {
            "id": self.__id_producto,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }

    # Representación en texto del objeto
    def __str__(self):
        return f"ID: {self.__id_producto} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"


# ==========================================
# CLASE INVENTARIO
# ==========================================
class Inventario:
    def __init__(self, archivo="inventario.json"):
        # Utilizamos un DICCIONARIO para gestionar los productos.
        # La clave es el ID del producto y el valor es el objeto Producto.
        # Esto permite búsquedas y eliminaciones muy eficientes (O(1)).
        self.productos = {}
        self.archivo = archivo
        self.cargar_desde_archivo()  # Carga los datos automáticamente al iniciar

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("❌ Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.get_id()] = producto
            self.guardar_en_archivo()
            print("✅ Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("✅ Producto eliminado con éxito.")
        else:
            print("❌ Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            self.guardar_en_archivo()
            print("✅ Producto actualizado con éxito.")
        else:
            print("❌ Error: Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        # Usamos una lista por comprensión para buscar coincidencias parciales
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]

        if encontrados:
            print("\n--- Resultados de la búsqueda ---")
            for p in encontrados:
                print(p)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("\n--- Inventario Completo ---")
            for p in self.productos.values():
                print(p)

    # ==========================================
    # MANEJO DE ARCHIVOS (Persistencia)
    # ==========================================
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, 'w') as f:
                # Convertimos los objetos Producto a diccionarios simples para JSON
                data = {id_p: p.to_dict() for id_p, p in self.productos.items()}
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"❌ Error al guardar en el archivo: {e}")

    def cargar_desde_archivo(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as f:
                    data = json.load(f)
                    # Reconstruimos los objetos Producto a partir de los datos leídos
                    for id_p, p_data in data.items():
                        self.productos[id_p] = Producto(
                            p_data["id"],
                            p_data["nombre"],
                            p_data["cantidad"],
                            p_data["precio"]
                        )
            except Exception as e:
                print(f"❌ Error al cargar el archivo: {e}")


# ==========================================
# INTERFAZ DE USUARIO (Menú en Consola)
# ==========================================
def menu_principal():
    inventario = Inventario()

    while True:
        print("\n" + "=" * 40)
        print("  SISTEMA DE GESTIÓN DE INVENTARIO")
        print("=" * 40)
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        print("=" * 40)

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_p = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre: ")
            try:
                cant = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                nuevo_producto = Producto(id_p, nombre, cant, precio)
                inventario.añadir_producto(nuevo_producto)
            except ValueError:
                print("❌ Error: La cantidad debe ser un entero y el precio un número.")

        elif opcion == '2':
            id_p = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_p)

        elif opcion == '3':
            id_p = input("Ingrese el ID del producto a actualizar: ")
            print("Deje en blanco si no desea actualizar el campo.")
            cant_str = input("Nueva cantidad: ")
            precio_str = input("Nuevo precio: ")

            cant = int(cant_str) if cant_str else None
            precio = float(precio_str) if precio_str else None

            if cant is not None or precio is not None:
                inventario.actualizar_producto(id_p, cant, precio)
            else:
                print("No se realizaron cambios.")

        elif opcion == '4':
            nombre = input("Ingrese el nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_todos()

        elif opcion == '6':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu_principal()