import tkinter as tk
from tkinter import messagebox


class AplicacionGUI:
    def __init__(self, root):
        """
        Constructor de la clase: Configura la ventana principal y todos los componentes.
        """
        self.root = root
        # 1. Ventana principal con título descriptivo
        self.root.title("Gestor de Datos - Interfaz Básica")
        self.root.geometry("350x400")  # Ancho x Alto de la ventana
        self.root.resizable(False, False)  # Evita que se cambie el tamaño de la ventana

        # --- Creación de Componentes GUI ---

        # 2. Etiqueta (Label)
        self.label_instruccion = tk.Label(root, text="Ingrese un nuevo dato o tarea:")
        self.label_instruccion.pack(pady=10)  # pack() ubica el elemento. pady da espacio vertical.

        # 3. Campo de texto (Entry)
        self.entrada_dato = tk.Entry(root, width=35)
        self.entrada_dato.pack(pady=5)

        # Contenedor (Frame) para agrupar los botones horizontalmente
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        # 4. Botón "Agregar" (Vinculado al evento self.agregar_dato)
        self.btn_agregar = tk.Button(frame_botones, text="Agregar", command=self.agregar_dato, bg="#4CAF50", fg="white")
        self.btn_agregar.grid(row=0, column=0, padx=10)

        # 5. Botón "Limpiar" (Vinculado al evento self.limpiar_datos)
        self.btn_limpiar = tk.Button(frame_botones, text="Limpiar Lista", command=self.limpiar_datos, bg="#f44336",
                                     fg="white")
        self.btn_limpiar.grid(row=0, column=1, padx=10)

        # 6. Lista para mostrar datos (Listbox)
        self.lista_datos = tk.Listbox(root, width=40, height=12)
        self.lista_datos.pack(pady=10)

    # --- Funcionalidad y Manejo de Eventos ---

    def agregar_dato(self):
        """
        Evento desencadenado al presionar el botón 'Agregar'.
        Toma el texto del Entry y lo coloca en el Listbox.
        """
        # Obtenemos el texto ingresado por el usuario
        nuevo_dato = self.entrada_dato.get()

        # Validamos que el texto no esté vacío (solo espacios en blanco)
        if nuevo_dato.strip() != "":
            # Agregamos el dato al final de la lista
            self.lista_datos.insert(tk.END, nuevo_dato)
            # Limpiamos el campo de texto para el siguiente ingreso
            self.entrada_dato.delete(0, tk.END)
        else:
            # Mostramos una alerta si intenta agregar algo vacío
            messagebox.showwarning("Advertencia", "Por favor, ingrese algún texto antes de agregar.")

    def limpiar_datos(self):
        """
        Evento desencadenado al presionar el botón 'Limpiar Lista'.
        Borra toda la información de la interfaz.
        """
        # Borra todos los elementos de la lista, desde el índice 0 hasta el final
        self.lista_datos.delete(0, tk.END)
        # Aseguramos que el campo de texto también quede vacío
        self.entrada_dato.delete(0, tk.END)


# --- Bloque principal de ejecución ---
if __name__ == "__main__":
    # Creamos la ventana principal
    ventana_principal = tk.Tk()
    # Instanciamos nuestra aplicación
    app = AplicacionGUI(ventana_principal)
    # Iniciamos el bucle principal (el programa se queda esperando que el usuario interactúe)
    ventana_principal.mainloop()