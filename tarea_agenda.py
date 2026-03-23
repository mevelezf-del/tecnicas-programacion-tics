import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Importamos el DatePicker


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi Agenda Personal")
        self.root.geometry("600x450")

        # --- ORGANIZACIÓN CON CONTENEDORES (Frames) ---
        # Frame para la entrada de datos (arriba)
        self.frame_entradas = tk.Frame(self.root, padx=10, pady=10)
        self.frame_entradas.pack(fill="x")

        # Frame para la visualización de la lista (centro)
        self.frame_lista = tk.Frame(self.root, padx=10, pady=10)
        self.frame_lista.pack(fill="both", expand=True)

        # Frame para los botones de acción (abajo)
        self.frame_botones = tk.Frame(self.root, padx=10, pady=10)
        self.frame_botones.pack(fill="x")

        # --- COMPONENTES DE ENTRADA (Labels, Entry, DatePicker) ---
        # Fecha
        tk.Label(self.frame_entradas, text="Fecha:").grid(row=0, column=0, sticky="w", pady=5)
        # Implementación del DatePicker con DateEntry
        self.entrada_fecha = DateEntry(self.frame_entradas, width=12, background='darkblue',
                                       foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.entrada_fecha.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Hora
        tk.Label(self.frame_entradas, text="Hora (HH:MM):").grid(row=1, column=0, sticky="w", pady=5)
        self.entrada_hora = tk.Entry(self.frame_entradas, width=15)
        self.entrada_hora.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Descripción
        tk.Label(self.frame_entradas, text="Descripción:").grid(row=2, column=0, sticky="w", pady=5)
        self.entrada_desc = tk.Entry(self.frame_entradas, width=40)
        self.entrada_desc.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # --- COMPONENTE DE VISUALIZACIÓN (TreeView) ---
        # Definimos las columnas
        columnas = ("fecha", "hora", "descripcion")
        self.tree = ttk.Treeview(self.frame_lista, columns=columnas, show="headings")

        # Configuramos los encabezados
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")

        # Configuramos el ancho de las columnas
        self.tree.column("fecha", width=100, anchor="center")
        self.tree.column("hora", width=100, anchor="center")
        self.tree.column("descripcion", width=350, anchor="w")

        self.tree.pack(fill="both", expand=True)

        # --- BOTONES DE ACCIÓN ---
        self.btn_agregar = tk.Button(self.frame_botones, text="Agregar Evento", bg="#4CAF50", fg="white",
                                     command=self.agregar_evento)
        self.btn_agregar.pack(side="left", padx=5)

        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", bg="#f44336", fg="white",
                                      command=self.eliminar_evento)
        self.btn_eliminar.pack(side="left", padx=5)

        self.btn_salir = tk.Button(self.frame_botones, text="Salir", command=self.root.quit)
        self.btn_salir.pack(side="right", padx=5)

    # --- MANEJO DE EVENTOS (Funciones) ---
    def agregar_evento(self):
        # 1. Obtenemos los datos de los campos de entrada
        fecha = self.entrada_fecha.get()
        hora = self.entrada_hora.get()
        desc = self.entrada_desc.get()

        # 2. Validamos que los campos no estén vacíos
        if not hora or not desc:
            messagebox.showwarning("Campos incompletos", "Por favor, ingresa la hora y la descripción.")
            return

        # 3. Insertamos los datos en el TreeView
        self.tree.insert("", "end", values=(fecha, hora, desc))

        # 4. Limpiamos los campos de entrada de texto (la fecha se mantiene)
        self.entrada_hora.delete(0, tk.END)
        self.entrada_desc.delete(0, tk.END)

        messagebox.showinfo("Éxito", "Evento agregado correctamente.")

    def eliminar_evento(self):
        # 1. Obtenemos el elemento seleccionado en el TreeView
        seleccion = self.tree.selection()

        if not seleccion:
            messagebox.showwarning("Sin selección", "Por favor, selecciona un evento de la lista para eliminar.")
            return

        # 2. Mostramos el diálogo de confirmación (Requisito Opcional)
        confirmar = messagebox.askyesno("Confirmar Eliminación",
                                        "¿Estás seguro de que deseas eliminar el evento seleccionado?")

        # 3. Si el usuario confirma, eliminamos el evento
        if confirmar:
            for item in seleccion:
                self.tree.delete(item)


# --- BLOQUE PRINCIPAL ---
if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = AgendaApp(ventana_principal)
    ventana_principal.mainloop()