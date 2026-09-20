# Fundamentos de interfaces graficas de usuario con Tkinter

## Tema

Componentes y contenedores en una aplicación de biblioteca con Tkinter.

## Objetivo de aprendizaje

Evolucionar el proyecto de la Semana 13 sin cambiar su arquitectura principal. La aplicación conserva el inicio de sesión, los modelos, los servicios y la persistencia en JSON, pero ahora organiza mejor la interfaz mediante Frameformularios LabelFrame, tablas e iconos.

## Evolucion del programa

En el proyecto se implemento, la incorporacón de iconos y logotipo que se guardaron en la carpeta assets/logo; ademas se incorporó la función de agregar, eliminar productos; las nuevas funciones se centrarón en mejorar la experiencia del usuario basada en la interfaz gráfica.



## Estructura

restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── assets/                
├── main.py
└── README.md

## Organización del logo
El logo principal debe guardarse en:

restaurante_app/assets/logo/logo.png
El icono de ventana debe guardarse en:

restaurante_app/assets/logo/icono.png
En este proyecto, logo.pngmide 150x150 px. Para que no ocupe demasiado espacio, en el login se reduce con subsample(2, 2)y en el menú lateral se reduce con subsample(3, 3).

El archivo icono.pngmide 64x64 px. Ese tamaño funciona bien para el icono de la ventana.

La integración se realiza en tres lugares:

main.py: configura el icono de la ventana usando icono.pngcon root.iconphoto(...).

ui/login_view.py: carga logo.pngcon tk.PhotoImagey lo muestra sobre el titulo del login.

ui/main_view.py: reutiliza logo.png, lo reduce y lo muestra en el menú lateral.

Importante: las rutas son relativas al proyecto. No se usan rutas absolutas del equipo, por eso el proyecto puede mover de carpeta sin romper la carga de imágenes.

Para esta practica se usa PNG porque es mas simple de explicar con tk.PhotoImage. El formato .icopuede usarse en Windows, pero debe ser un icono real y no un PNG renombrado.

Pantallas principales
LoginView: pantalla de inicio de sesión. Usa el logo del sistema, Entrypara usuario y contraseña, y un botón con command=para validar el acceso.

Inicio: panel de resumen. Muestra cuántos usuarios y libros existen en los archivos JSON.

Usuarios: pantalla de consulta. Muestra los usuarios registrados en una tabla, sin CRUD, para mantener esta sección sencilla.

Libros: pantalla de gestión. Incluye formulario, botones y tabla para registrar, cargar, actualizar y eliminar productos.

Componentes Tkinter utilizados
Label: productos.

Entry: campos de entrada para iniciar sesión y formulario de libros.

ttk.Button: botones de navegación y acciones.

ttk.Treeview: tablas de usuarios y productos.

ttk.Scrollbar: barra de desplazamiento para las tablas.

messagebox: mensajes simples de confirmación o error.

Contenedores utilizados
Tk: ventana principal de la aplicación.

Frame: separa el menú lateral, el contenido principal, tarjetas, barra de estado y grupos internos.

LabelFrame: agrupa visualmente el formulario de productos y las tablas.

Uso de gestores de geometría
La ventana principal se usa pack()para separar el menú lateral y el contenido.

El formulario de productos usa grid()para alinear etiquetas y entradas.

No se mezcla pack()y grid()dentro del mismo contenedor.

Funcionamiento del CRUD de productos
El CRUD se realiza desde la pantalla productos.

Registrar: crea un producto nuevo si el código no está repetido.
Cargar por codigo: busca un producto por su código y llena el formulario.
Actualizar: modifica nombre y precio de un producto existente.
Eliminar: borra un producto existente por código.
Limpiar: vacia el formulario.
Cada operación usa los métodos de RestauranteServicio, guarda los cambios en datos/productos.jsony refresca la tabla.

Interacción concommand=
Los botones se usan command=para ejecutar métodos concretos. Esta semana no profundizamos en el manejo avanzado de eventos.

No se utiliza:

bind()
doble clic
selección automática desde la tabla
eventos de teclado o mouse
edición directa dentro delTreeview
Eso queda reservado para la siguiente semana sobre eventos.