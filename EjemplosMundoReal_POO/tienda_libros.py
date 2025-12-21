# CASO DEL MUNDO REAL: SISTEMA DE GESTIÓN DE UNA TIENDA DE LIBROS
# Descripción: Este programa modela una librería física. 
# Tenemos la clase 'Libro' que representa los productos físicos con sus atributos (título, autor, precio).
# Tenemos la clase 'Tienda' que gestiona el inventario y realiza la acción de venta.

class Libro:
    """Clase que representa un libro físico en la tienda."""
    
    def __init__(self, titulo, autor, precio, stock):
        # Atributos de instancia (características del objeto)
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.stock = stock # Cantidad de libros disponibles

    def mostrar_info(self):
        """Método para mostrar los detalles del libro."""
        return f"Título: {self.titulo}, Autor: {self.autor}, Precio: ${self.precio}, Stock: {self.stock}"

class Tienda:
    """Clase que representa la tienda que gestiona los libros."""
    
    def __init__(self):
        self.inventario = [] # Lista para guardar los objetos tipo Libro

    def agregar_libro(self, libro):
        """Recibe un objeto Libro y lo agrega al inventario."""
        self.inventario.append(libro)
        print(f"El libro '{libro.titulo}' ha sido agregado al inventario.")

    def vender_libro(self, titulo_libro):
        """Busca un libro por título y reduce su stock si es posible."""
        for libro in self.inventario:
            if libro.titulo == titulo_libro:
                if libro.stock > 0:
                    libro.stock -= 1
                    print(f"Venta realizada: Has comprado '{libro.titulo}'. Precio: ${libro.precio}")
                    print(f"Quedan {libro.stock} unidades disponibles.")
                else:
                    print(f"Lo sentimos, el libro '{libro.titulo}' está agotado.")
                return # Salimos del método tras encontrar el libro
        print(f"El libro '{titulo_libro}' no se encuentra en el inventario.")

# --- EJECUCIÓN DEL PROGRAMA ---
if __name__ == "__main__":
    # 1. Crear la tienda
    mi_libreria = Tienda()

    # 2. Crear objetos Libro
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 25.00, 5)
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 15.50, 2)

    # 3. Interacción: Agregar libros a la tienda
    mi_libreria.agregar_libro(libro1)
    mi_libreria.agregar_libro(libro2)

    print("\n--- Iniciando Ventas ---\n")

    # 4. Interacción: Realizar ventas
    mi_libreria.vender_libro("Cien Años de Soledad")
    mi_libreria.vender_libro("El Principito")
    
    # Intento de comprar un libro que no existe
    mi_libreria.vender_libro("Harry Potter")