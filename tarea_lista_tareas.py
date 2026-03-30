import tkinter as tk
from tkinter import messagebox


# --- Lógica de la Aplicación y Manejadores de Eventos ---

def add_task(event=None):
    """Añade una nueva tarea a la lista."""
    task = task_entry.get()
    # Verificamos que el campo no esté vacío
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)  # Limpiamos el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "Por favor, escribe una tarea.")


def complete_task(event=None):
    """Marca la tarea seleccionada como completada cambiando su apariencia visual."""
    try:
        # Obtenemos el índice de la tarea seleccionada
        selected_index = task_listbox.curselection()[0]
        task_text = task_listbox.get(selected_index)

        # Evitamos marcar una tarea que ya está completada
        if not task_text.startswith("✔️"):
            task_listbox.delete(selected_index)
            # Insertamos el nuevo texto con un checkmark
            task_listbox.insert(selected_index, f"✔️ {task_text}")
            # Cambiamos el color de la fuente a gris para reflejar el estado
            task_listbox.itemconfig(selected_index, {'fg': 'gray'})
            # Quitamos la selección para que se vea claramente el cambio
            task_listbox.selection_clear(0, tk.END)
    except IndexError:
        # Manejamos el error si el usuario hace clic en el botón sin seleccionar nada
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para completarla.")


def delete_task():
    """Elimina la tarea seleccionada de la lista."""
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminarla.")


# --- Interfaz Gráfica (GUI) ---

# Configuración principal de la ventana
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x450")
root.config(padx=20, pady=20)

# 1. Campo de entrada (Entry)
task_entry = tk.Entry(root, width=35, font=("Arial", 12))
task_entry.pack(pady=10)
# Evento: Presionar la tecla Enter para añadir la tarea
task_entry.bind("<Return>", add_task)

# 2. Botón para añadir
add_button = tk.Button(root, text="Añadir Tarea", command=add_task, bg="#4CAF50", fg="white",
                       font=("Arial", 10, "bold"))
add_button.pack(pady=5)

# 3. Componente de lista (Listbox) para mostrar las tareas
task_listbox = tk.Listbox(root, width=40, height=12, font=("Arial", 11), selectbackground="#cce5ff",
                          selectforeground="black")
task_listbox.pack(pady=15)
# Evento opcional: Hacer doble clic en un elemento para marcarlo como completado
task_listbox.bind("<Double-Button-1>", complete_task)

# Marco para agrupar los botones inferiores
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# 4. Botones para Completar y Eliminar
complete_button = tk.Button(button_frame, text="Marcar como Completada", command=complete_task, bg="#2196F3",
                            fg="white", font=("Arial", 10))
complete_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Eliminar Tarea", command=delete_task, bg="#f44336", fg="white",
                          font=("Arial", 10))
delete_button.pack(side=tk.RIGHT, padx=5)

# Bucle de ejecución de la aplicación
root.mainloop()