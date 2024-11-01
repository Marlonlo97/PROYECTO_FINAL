## Documentacion Externa
# Introducción
El **Editor de archivos de texto** es una herramienta intuitiva y eficiente desarrollada con Python utilizando la biblioteca Tkinter. Su objetivo es proporcionar un entorno de edición de texto que combine funcionalidad y facilidad de uso, permitiendo a los usuarios gestionar documentos de texto y código de manera sencilla. Este editor es ideal tanto para programadores como para cualquier persona que necesite un espacio para redactar, editar o revisar textos.

# Características Principales

- **Interfaz Gráfica Amigable:** La aplicación cuenta con una interfaz gráfica clara y accesible, diseñada para facilitar la navegación y el uso de sus funciones.
- **Soporte para Varios Formatos de Archivo:** Permite abrir, editar y guardar archivos en formatos de texto y código, incluyendo .txt, .cpp, .cs y .py.
- **Funciones de Edición Avanzadas:** Incluye funcionalidades como deshacer y rehacer, búsqueda de texto y resaltado de términos encontrados.
- **Personalización Visual:** La aplicación permite agregar un logotipo en la ventana principal, mejorando la experiencia del usuario y la personalización.
- **Menú de Ayuda Integrado:** Proporciona acceso a información sobre la aplicación y detalles sobre los desarrolladores.

# Estructura de la Aplicación

La aplicación se organiza en diferentes secciones, cada una con funcionalidades específicas:

**1. Interfaz de Usuario**
- **Ventana Principal:** Al iniciar la aplicación, se presenta una ventana con un área de texto central y un menú superior.
- **Área de Texto:** Utiliza un widget de texto desplazable (ScrolledText) que permite a los usuarios escribir y editar contenido. Esta área admite múltiples líneas y cuenta con la opción de deshacer cambios.
- **Logotipo:** Se puede visualizar un logotipo en la esquina superior de la ventana, personalizando la interfaz.
  
**2. Menú Principal**

El menú principal se divide en tres secciones: Archivo, Editar y Ayuda. Cada sección incluye varias opciones de funcionalidad.

**Menú Archivo**
- Abrir: Permite seleccionar un archivo existente para cargar su contenido en el área de texto. Soporta múltiples formatos de archivo.
- Guardar: Guarda los cambios en el archivo actualmente abierto.
- Guardar Como: Ofrece la opción de guardar el contenido del área de texto en un nuevo archivo, permitiendo al usuario elegir la ubicación y el nombre.
- Buscar: Facilita la búsqueda de palabras o frases dentro del texto. Si se encuentra el término, se resalta en rojo.
  
**Menú Editar**
- Deshacer: Permite revertir la última acción realizada en el área de texto.
- Rehacer: Restaura la acción que se había deshecho anteriormente.
  
**Menú Ayuda**
- Información: Muestra un cuadro de diálogo con detalles sobre la versión de la aplicación y el equipo de desarrollo.
- Manual de Usuario: Proporciona acceso a un manual que explica las funcionalidades y características del editor.
- Integrantes: Muestra la información de los miembros del equipo responsable del desarrollo de la aplicación.
  
## Uso del Editor de Documentos
**1. Abrir un Archivo**

Para abrir un archivo:
1.	Dirígete al menú Archivo.
2.	Selecciona la opción Abrir.
3.	Navega hasta la ubicación del archivo deseado y selecciónalo.
4.	Haz clic en Abrir. El contenido del archivo se cargará en el área de texto.
   
**2. Guardar Cambios**
   
Para guardar cambios en un archivo abierto:
1.	Dirígete al menú Archivo.
2.	Selecciona la opción Guardar. Si no hay un archivo abierto, recibirás una advertencia.

**3. Guardar Como**
   
Para guardar el contenido en un nuevo archivo:
1.	Ve al menú Archivo.
2.	Selecciona Guardar como.
3.	Elige la ubicación y proporciona un nombre para el nuevo archivo.
4.	Haz clic en Guardar.

**4. Buscar Texto**

Para buscar un término:
1.	Dirígete al menú Archivo.
2.	Selecciona Buscar.
3.	Ingresa la palabra o frase que deseas encontrar y presiona Aceptar. Si se encuentra el texto, se resaltará en rojo.

**5. Deshacer y Rehacer**

Para deshacer o rehacer acciones:
- Usa el menú Editar y selecciona Deshacer o Rehacer según sea necesario. Se mostrarán mensajes si no hay más acciones que deshacer o rehacer.

# Posibilidades de Mejora
La aplicación tiene una base sólida, pero se pueden implementar varias mejoras para aumentar su funcionalidad:
- Implementación de Deshacer y Rehacer: Completar estas funciones para mejorar la experiencia del usuario.
- Soporte para Más Formatos de Archivo: Ampliar las opciones de archivos soportados para incluir formatos adicionales como Markdown o archivos de configuración.
- Características Avanzadas de Edición: Incluir funcionalidades como formato de texto (negrita, cursiva), listas y otras herramientas de edición.
- Interfaz Más Rica: Mejorar la interfaz gráfica para hacerla más atractiva y fácil de usar.

# Conclusión
El Editor de archivos de texto es una aplicación robusta que ofrece una amplia gama de funcionalidades para la edición de texto. Con su interfaz amigable y soporte para varios formatos de archivo, es una herramienta valiosa para estudiantes, profesionales y cualquier persona que necesite gestionar documentos de manera efectiva. Este manual proporciona una guía completa para utilizar todas las funciones de la aplicación, asegurando una experiencia de usuario fluida y productiva.
