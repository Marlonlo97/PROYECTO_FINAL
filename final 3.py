#Aplicación con interfaz gráfica para leer un archivo de texto como .txt, .cpp, .cs, .py y otros.
import tkinter as tk 
from tkinter import filedialog, messagebox, simpledialog, scrolledtext
import os

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor De Documentos")
        self.file_path = None
        
        # Área de texto con opción de deshacer habilitada
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, undo=True)
        self.text_area.pack(expand=True, fill='both')
        
        # Menú
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        
        # Menú Archivo
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Guardar", command=self.save_file)
        self.file_menu.add_command(label="Guardar como", command=self.save_as_file)
        self.file_menu.add_command(label="Buscar", command=self.search_text)
        
        # Menú Editar
        self.edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Editar", menu=self.edit_menu)
        self.edit_menu.add_command(label="Deshacer", command=self.undo)
        self.edit_menu.add_command(label="Rehacer", command=self.redo)
        
        # Menú Ayuda
        self.help_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Ayuda", menu=self.help_menu)
        self.help_menu.add_command(label="Información", command=self.show_info)
        self.help_menu.add_command(label="Manual de usuario", command=self.open_manual)
        self.help_menu.add_command(label="Integrantes", command=self.show_members)
        
    def open_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt"),
                                                                ("Archivos C/C++", "*.cpp"),
                                                                ("Archivos C#", "*.cs"),
                                                                ("Archivos Python", "*.py"),
                                                                ("Todos los archivos", "*.*")])
        if self.file_path:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)

    def save_file(self):
        if self.file_path:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)
        else:
            messagebox.showwarning("Advertencia", "No hay archivo abierto para guardar.")

    def save_as_file(self):
        self.file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                       filetypes=[("Archivos de texto", "*.txt"),
                                                                  ("Archivos C/C++", "*.cpp"),
                                                                  ("Archivos C#", "*.cs"),
                                                                  ("Archivos Python", "*.py"),
                                                                  ("Todos los archivos", "*.*")])
        if self.file_path:
            self.save_file()

    def search_text(self):
        search_term = simpledialog.askstring("Buscar", "Ingrese la palabra o frase a buscar:")
        if search_term:
            content = self.text_area.get(1.0, tk.END)
            start_index = content.find(search_term)
            if start_index != -1:
                self.text_area.tag_add("found", f"1.0 + {start_index} chars", f"1.0 + {start_index + len(search_term)} chars")
                self.text_area.tag_config("found", foreground="red")
            else:
                messagebox.showinfo("Buscar", "No se encontró el texto.")

    def undo(self):
        try:
            self.text_area.edit_undo()
        except tk.TclError:
            messagebox.showinfo("Deshacer", "No hay más acciones para deshacer.")

    def redo(self):
        try:
            self.text_area.edit_redo()
        except tk.TclError:
            messagebox.showinfo("Rehacer", "No hay más acciones para rehacer.")

    def show_info(self):
        messagebox.showinfo("Información", "Editor de texto\nVersion 1.00\nDesarrollado por Grupo 3.")

    def open_manual(self):
        os.startfile("ruta/al/manual.pdf")  # Cambia esta ruta por la correcta

    def show_members(self):
        messagebox.showinfo("Integrantes", "Marlon Armando López Díaz - 7690-24-23476\nJosé Luis Castillo Virula - 7690-24-18043\nGrupo No. 3")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()
