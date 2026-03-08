class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # REQUISITO: Utiliza una tupla para almacenar el autor y el título (inmutables)
        self.info_basica = (autor, titulo)
        self.categoria = categoria
        self.isbn = isbn

    # Métodos auxiliares para acceder fácilmente a la tupla
    @property
    def autor(self):
        return self.info_basica[0]

    @property
    def titulo(self):
        return self.info_basica[1]

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # REQUISITO: Utiliza listas para gestionar los libros prestados a cada usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        # REQUISITO: Diccionario para almacenar libros disponibles (ISBN como clave, Libro como valor)
        self.libros_disponibles = {}
        # REQUISITO: Conjunto para manejar los IDs de usuarios únicos
        self.ids_usuarios = set()
        # Diccionario adicional para acceder a los objetos Usuario rápidamente
        self.usuarios_registrados = {}

    def añadir_libro(self, libro):
        """Añade un libro a la biblioteca si el ISBN no existe."""
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"✅ Libro añadido: {libro.titulo}")
        else:
            print(f"⚠️ El libro con ISBN {libro.isbn} ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        """Quita un libro del catálogo de disponibles."""
        if isbn in self.libros_disponibles:
            libro_eliminado = self.libros_disponibles.pop(isbn)
            print(f"🗑️ Libro eliminado: {libro_eliminado.titulo}")
        else:
            print("⚠️ Libro no encontrado.")

    def registrar_usuario(self, usuario):
        """Registra un nuevo usuario asegurando que el ID sea único usando un conjunto."""
        if usuario.id_usuario not in self.ids_usuarios:
            self.ids_usuarios.add(usuario.id_usuario)
            self.usuarios_registrados[usuario.id_usuario] = usuario
            print(f"✅ Usuario registrado: {usuario.nombre}")
        else:
            print(f"⚠️ Error: El ID de usuario '{usuario.id_usuario}' ya está en uso.")

    def dar_baja_usuario(self, id_usuario):
        """Da de baja a un usuario si no tiene libros pendientes por devolver."""
        if id_usuario in self.ids_usuarios:
            usuario = self.usuarios_registrados[id_usuario]
            if len(usuario.libros_prestados) > 0:
                print(f"⚠️ {usuario.nombre} no puede darse de baja porque tiene libros prestados.")
            else:
                self.ids_usuarios.remove(id_usuario)
                del self.usuarios_registrados[id_usuario]
                print(f"🗑️ Usuario con ID {id_usuario} dado de baja.")
        else:
            print("⚠️ Usuario no encontrado.")

    def prestar_libro(self, isbn, id_usuario):
        """Pasa un libro de disponibles a la lista de prestados del usuario."""
        if isbn in self.libros_disponibles and id_usuario in self.ids_usuarios:
            libro = self.libros_disponibles.pop(isbn)  # Se saca de los disponibles
            usuario = self.usuarios_registrados[id_usuario]
            usuario.libros_prestados.append(libro)
            print(f"📖 Libro prestado: '{libro.titulo}' a {usuario.nombre}.")
        elif isbn not in self.libros_disponibles:
            print("⚠️ El libro no está disponible actualmente.")
        else:
            print("⚠️ Usuario no registrado.")

    def devolver_libro(self, isbn, id_usuario):
        """Devuelve un libro del usuario a la lista de libros disponibles."""
        if id_usuario in self.ids_usuarios:
            usuario = self.usuarios_registrados[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro  # Vuelve a estar disponible
                    print(f"↩️ Libro devuelto: '{libro.titulo}' por {usuario.nombre}.")
                    return
            print("⚠️ El usuario no tiene este libro prestado.")
        else:
            print("⚠️ Usuario no encontrado.")

    def buscar_libro(self, busqueda):
        """Busca libros por título, autor o categoría en los libros disponibles."""
        busqueda = busqueda.lower()
        resultados = []
        for libro in self.libros_disponibles.values():
            if (busqueda in libro.titulo.lower() or
                    busqueda in libro.autor.lower() or
                    busqueda in libro.categoria.lower()):
                resultados.append(libro)

        if resultados:
            print("\n🔍 Resultados de la búsqueda:")
            for libro in resultados:
                print(f" - {libro}")
        else:
            print("\n🔍 No se encontraron libros con esa búsqueda.")

    def listar_libros_prestados(self, id_usuario):
        """Muestra la lista de libros que tiene un usuario en este momento."""
        if id_usuario in self.ids_usuarios:
            usuario = self.usuarios_registrados[id_usuario]
            print(f"\n📚 Libros actualmente prestados a {usuario.nombre}:")
            if not usuario.libros_prestados:
                print(" - Ninguno.")
            for libro in usuario.libros_prestados:
                print(f" - {libro.titulo} (ISBN: {libro.isbn})")
        else:
            print("⚠️ Usuario no encontrado.")


# --- PRUEBAS DEL SISTEMA (EJECUCIÓN) ---
if __name__ == "__main__":
    # 1. Crear la biblioteca
    mi_biblioteca = Biblioteca()

    # 2. Crear libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "12345")
    libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", "67890")
    libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", "11111")

    # 3. Crear usuarios
    user1 = Usuario("Ana Gómez", "U001")
    user2 = Usuario("Carlos Ruiz", "U002")

    print("\n--- AÑADIR LIBROS Y REGISTRAR USUARIOS ---")
    mi_biblioteca.añadir_libro(libro1)
    mi_biblioteca.añadir_libro(libro2)
    mi_biblioteca.añadir_libro(libro3)

    mi_biblioteca.registrar_usuario(user1)
    mi_biblioteca.registrar_usuario(user2)

    print("\n--- BÚSQUEDA DE LIBROS ---")
    mi_biblioteca.buscar_libro("orwell")  # Búsqueda por autor
    mi_biblioteca.buscar_libro("novela")  # Búsqueda por categoría

    print("\n--- PRESTAR LIBROS ---")
    mi_biblioteca.prestar_libro("12345", "U001")
    mi_biblioteca.prestar_libro("67890", "U001")

    print("\n--- LISTAR LIBROS PRESTADOS ---")
    mi_biblioteca.listar_libros_prestados("U001")

    print("\n--- INTENTAR DAR DE BAJA A UN USUARIO CON LIBROS ---")
    mi_biblioteca.dar_baja_usuario("U001")

    print("\n--- DEVOLVER LIBROS ---")
    mi_biblioteca.devolver_libro("12345", "U001")
    mi_biblioteca.listar_libros_prestados("U001")

    print("\n--- DAR DE BAJA USUARIO ---")
    mi_biblioteca.dar_baja_usuario("U002")