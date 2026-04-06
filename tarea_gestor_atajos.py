import tkinter as tk
from tkinter import messagebox


# --- 1. Funciones de Lógica ---

def add_task(event=None):
    tarea = task_entry.get().strip()
    if tarea:
        task_listbox.insert(tk.END, tarea)
        # Aseguramos que la tarea nueva se vea en color negro
        task_listbox.itemconfig(tk.END, {'fg': 'black'})
        task_entry.delete(0, tk.END)
    else:
        # Solo muestra advertencia si se hace clic en el botón (no si se presiona Enter al vacío)
        if not event:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")


def complete_task(event=None):
    try:
        seleccion = task_listbox.curselection()[0]
        tarea_texto = task_listbox.get(seleccion)

        # Evitar marcar dos veces la misma tarea
        if not tarea_texto.startswith("✓ "):
            task_listbox.delete(seleccion)
            task_listbox.insert(seleccion, f"✓ {tarea_texto}")
            # Feedback visual: cambia la letra a gris para indicar que está lista
            task_listbox.itemconfig(seleccion, {'fg': 'gray'})
            task_listbox.selection_set(seleccion)
    except IndexError:
        if not event:
            messagebox.showwarning("Advertencia", "Selecciona una tarea primero.")


def delete_task(event=None):
    try:
        seleccion = task_listbox.curselection()[0]
        task_listbox.delete(seleccion)
    except IndexError:
        if not event:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")


def close_app(event=None):
    root.destroy()


# --- 2. Configuración de la Ventana Principal ---
root = tk.Tk()
root.title("Gestión de Tareas con Atajos")
root.geometry("450x450")
root.config(padx=20, pady=20)

# --- 3. Interfaz Gráfica (Widgets) ---

# Marco superior para entrada y botón de añadir
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

task_entry = tk.Entry(frame_entrada, width=30, font=("Arial", 12))
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame_entrada, text="Añadir Tarea", command=add_task, bg="#4CAF50", fg="white",
                       font=("Arial", 10, "bold"))
add_button.pack(side=tk.LEFT)

# Lista de tareas
task_listbox = tk.Listbox(root, width=45, height=12, font=("Arial", 11), selectbackground="#cce5ff",
                          selectforeground="black")
task_listbox.pack(pady=10)

# El evento de doble clic que ya tenías (¡es un gran detalle extra!)
task_listbox.bind("<Double-Button-1>", complete_task)

# Marco inferior para botones de acción
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

complete_button = tk.Button(button_frame, text="Completar (C)", command=complete_task, bg="#2196F3", fg="white",
                            font=("Arial", 10))
complete_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Eliminar (D / Supr)", command=delete_task, bg="#f44336", fg="white",
                          font=("Arial", 10))
delete_button.pack(side=tk.LEFT, padx=5)

# --- 4. Atajos de Teclado (Requisito Principal de la Tarea) ---
root.bind("<Return>", add_task)  # Tecla Enter
root.bind("<c>", complete_task)  # Tecla c minúscula
root.bind("<C>", complete_task)  # Tecla C mayúscula
root.bind("<Delete>", delete_task)  # Tecla Suprimir (Del)
root.bind("<d>", delete_task)  # Tecla d minúscula
root.bind("<D>", delete_task)  # Tecla D mayúscula
root.bind("<Escape>", close_app)  # Tecla Escape para salir

# Bucle de ejecución
root.mainloop()