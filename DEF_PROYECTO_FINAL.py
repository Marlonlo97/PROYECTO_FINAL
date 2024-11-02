import tkinter as tk 
from tkinter import filedialog, messagebox, simpledialog, scrolledtext, PhotoImage
import os

class EditorDeTexto:
    def __init__(self, root):
        """Inicializa la aplicación del editor de texto.
        
        Args:
            root: La ventana principal de la aplicación.
        """
        self.root = root
        self.root.title("Editor De Archivos de Texto") # Indica el titulo o nombre que lleva la aplicacion 
        self.file_path = None  # Esta seccion almacena la ruta del archivo abierto
        
        # Agrega el logotipo de la Universidad Mariano Galvez en la parte superior izquierda de la ventana 
        self.logo = PhotoImage(file="C:/Users/Mgiro/OneDrive - Universidad Mariano Gálvez/Segundo Semestre/algoritmos/proyecto final/logo.png")  # Llama a la ruta en donde se encuentra el logotipo a utilizar 
        self.root.iconphoto(True, self.logo)  # Establece el ícono de la ventana
        
        # Habilita el area de texto con opción de deshacer habilitada
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, undo=True, font=("Arial", 12))
        self.text_area.pack(expand=True, fill='both')  # Se expande y llena la ventana

        # Menú principal
        self.menu = tk.Menu(self.root)  # Estilo básico del menú
        self.root.config(menu=self.menu)  # Configura el menú en la ventana principal
        
        # Menú Archivo con opciones
        self.file_menu = tk.Menu(self.menu, tearoff=0, bg="white", fg="black", font=("Arial", 9)) # Establece el tamaño, color y fuente de la opcion Archivo
        self.menu.add_cascade(label="Archivo", menu=self.file_menu)  # Agrega el menú Archivo
        
        # Comandos del menú Archivo
        self.file_menu.add_command(label="Abrir", command=self.open_file) # Permite la busqueda de los archivos que se desea abrir 
        self.file_menu.add_command(label="Guardar", command=self.save_file) # Permite almacenar un nuevo archivo o un archivo ya existente 
        self.file_menu.add_command(label="Guardar como", command=self.save_as_file) # Permite almacenar un documento en un lugar diferente o como diferente tipo de texto
        self.file_menu.add_command(label="Buscar", command=self.search_text) # Permite buscar palabras o frases que se encuentra dentro del archivo abierto
        
        # Menú Editar
        self.edit_menu = tk.Menu(self.menu, tearoff=0, bg="white", fg="black", font=("Arial", 9)) # Establece el tamaño, color y fuente de la opcion Editar
        self.menu.add_cascade(label="Editar", menu=self.edit_menu)  # Agrega el menú Editar
        
        # Comandos del menú Editar
        self.edit_menu.add_command(label="Deshacer", command=self.undo) # Permite deshacer todo cambio que no haya sido guardado 
        self.edit_menu.add_command(label="Rehacer", command=self.redo) # Permite rehacer cualquier cambio que haya sido eliminado que no haya sido guardado 
        
        # Menú Ayuda
        self.help_menu = tk.Menu(self.menu, tearoff=0, bg="white", fg="black", font=("Arial", 9)) # Establece el tamaño, color y fuente de la opcion Ayuda
        self.menu.add_cascade(label="Ayuda", menu=self.help_menu)  # Agrega el menú Ayuda
        
        # Comandos del menú Ayuda
        self.help_menu.add_command(label="Información", command=self.show_info) # Brinda la informcion de la aplicacion como el nombre y la version 
        self.help_menu.add_command(label="Manual de usuario", command=self.open_manual) # Permite abrir un documento en donde se encontrara las instrucciones de como utilizar la aplicacion 
        self.help_menu.add_command(label="Integrantes", command=self.show_members) # Muestra la informacion de los creadores de la aplicacion

    def open_file(self):
        """Abre un archivo de texto de tipo .txt, .cpp, .cs, .py, y carga su contenido en el área de texto."""
        self.file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt"),
                                                                ("Archivos C/C++", "*.cpp"),
                                                                ("Archivos C#", "*.cs"),
                                                                ("Archivos Python", "*.py"),
                                                                ("Todos los archivos", "*.*")])
        if self.file_path:  # Si se selecciona un archivo
            with open(self.file_path, 'r', encoding='utf-8') as file:
                content = file.read()  # Lee el contenido del archivo
                self.text_area.delete(1.0, tk.END)  # Limpia el área de texto
                self.text_area.insert(tk.END, content)  # Inserta el contenido

    def save_file(self):
        """Guarda el contenido del área de texto en el archivo abierto."""
        if self.file_path:  # Verifica si hay un archivo abierto
            with open(self.file_path, 'w', encoding='utf-8') as file:
                content = self.text_area.get(1.0, tk.END)  # Obtiene el contenido del área de texto
                file.write(content)  # Escribe el contenido en el archivo
        else:
            messagebox.showwarning("Advertencia", "No hay archivo abierto para guardar.") # Emerge una ventana en la cual se indica que no hay un archivo para guardar

    def save_as_file(self):
        """Abre un diálogo para guardar el contenido en un nuevo archivo."""
        self.file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                       filetypes=[("Archivos de texto", "*.txt"),
                                                                  ("Archivos C/C++", "*.cpp"),
                                                                  ("Archivos C#", "*.cs"),
                                                                  ("Archivos Python", "*.py"),
                                                                  ("Todos los archivos", "*.*")])
        if self.file_path:  # Si se selecciona un archivo
            self.save_file()  # Llama al método para guardar el archivo

    def search_text(self):
        """Busca un término en el área de texto y resalta la coincidencia."""
        search_term = simpledialog.askstring("Buscar", "Ingrese la palabra o frase a buscar:")
        if search_term:  # Si se ingresa un término de búsqueda
            content = self.text_area.get(1.0, tk.END)  # Obtiene el contenido
            start_index = content.find(search_term)  # Busca el término
            if start_index != -1:  # Si se encuentra el término
                self.text_area.tag_add("found", f"1.0 + {start_index} chars", 
                                        f"1.0 + {start_index + len(search_term)} chars")
                self.text_area.tag_config("found", foreground="red")  # Resalta en rojo
            else:
                messagebox.showinfo("Buscar", "No se encontró el texto.")  # Mensaje si no se encuentra el término a buscar

    def undo(self):
        """Deshace la última acción en el área de texto."""
        try:
            self.text_area.edit_undo()  # Intenta deshacer la acción
        except tk.TclError:
            messagebox.showinfo("Deshacer", "No hay más acciones para deshacer.")

    def redo(self):
        """Rehace la última acción deshecha en el área de texto."""
        try:
            self.text_area.edit_redo()  # Intenta rehacer la acción
        except tk.TclError:
            messagebox.showinfo("Rehacer", "No hay más acciones para rehacer.")

    def show_info(self):
        """Muestra información sobre la aplicación."""
        messagebox.showinfo("Información", "Editor de texto\nVersion 1.00\nDesarrollado por Grupo 3.")

    def open_manual(self):
        """Abre el manual de usuario en un archivo PDF."""
        os.startfile("ruta/al/manual.pdf")  # Cambia esta ruta por la correcta

    def show_members(self):
        """Muestra los integrantes del grupo que desarrolló la aplicación."""
        messagebox.showinfo("Integrantes", "Marlon Armando López Díaz - 7690-24-23476\nJosé Luis Castillo Virula - 7690-24-18043\nGrupo No. 3")

if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = EditorDeTexto(root)  # Instancia la aplicación
    root.mainloop()  # Inicia el bucle principal de la interfaz gráfica