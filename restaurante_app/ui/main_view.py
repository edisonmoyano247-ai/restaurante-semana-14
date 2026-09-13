import tkinter as tk
from tkinter import messagebox, ttk


class MainView(tk.Frame):
    def __init__(self, master, restaurante_servicio, usuario_actual, al_cerrar_sesion):
        super().__init__(master, bg="#f7fafc")
        self.restaurante_servicio = restaurante_servicio
        self.usuario_actual = usuario_actual
        self.al_cerrar_sesion = al_cerrar_sesion
        self.contenido = None

        self.definir_estilos()
        self.construir_interfaz()

    def definir_estilos(self):
        # Define colores y estilos reutilizables de esta vista.
        self.color_fondo = "#f7fafc"
        self.color_encabezado = "#1f2a44"
        self.color_texto = "#243447"
        self.color_secundario = "#dbeafe"
        self.color_resaltado = "#2563eb"

        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure(
            "MenuApp.TButton",
            background=self.color_secundario,
            foreground=self.color_encabezado,
            font=("Arial", 10, "bold"),
            padding=(12, 8),
            borderwidth=0,
        )
        estilo.map("MenuApp.TButton", background=[("active", "#c7ddff")])
        estilo.configure(
            "CerrarSesion.TButton",
            background="#e11d48",
            foreground="#ffffff",
            font=("Arial", 10, "bold"),
            padding=(12, 8),
            borderwidth=0,
        )
        estilo.map("CerrarSesion.TButton", background=[("active", "#be123c")])

    def construir_interfaz(self):
        # Construye la pantalla principal de la aplicacion.
        encabezado = tk.Frame(self, bg=self.color_encabezado, padx=28, pady=18)
        encabezado.pack(fill="x")

        tk.Label(
            encabezado,
            text="Restaurante",
            bg=self.color_encabezado,
            fg="#ffffff",
            font=("Arial", 19, "bold"),
        ).pack(anchor="w")

        tk.Label(
            encabezado,
            text=f"Bienvenido, {self.usuario_actual.nombre}",
            bg=self.color_encabezado,
            fg="#17b124",
            font=("Arial", 11),
        ).pack(anchor="w", pady=(6, 0))

        barra = tk.Frame(self, bg=self.color_secundario, padx=18, pady=10)
        barra.pack(fill="x")

        self.crear_boton_menu(barra, "Productos", self.mostrar_productos)
        self.crear_boton_menu(barra, "Usuarios", self.mostrar_usuarios)
        self.crear_boton_menu(barra, "Pedidos en línea", self.mostrar_funcionalidad_pendiente)
        self.crear_boton_menu(barra, "Ventas", self.mostrar_funcionalidad_pendiente)

        ttk.Button(
            barra,
            text="Cerrar sesion",
            command=self.cerrar_sesion,
            style="CerrarSesion.TButton",
        ).pack(side="right")

        self.contenido = tk.Frame(self, bg=self.color_fondo, padx=28, pady=24)
        self.contenido.pack(fill="both", expand=True)

        self.mostrar_inicio()
        self.crear_barra_estado()

    def crear_boton_menu(self, contenedor, texto, comando):
        # Agrega una opcion visual en la barra superior.
        ttk.Button(
            contenedor,
            text=texto,
            command=comando,
            style="MenuApp.TButton",
        ).pack(side="left", padx=(0, 8))

    def limpiar_contenido(self):
        # Limpia el area central antes de mostrar una nueva seccion.
        assert self.contenido is not None

        for widget in self.contenido.winfo_children():
            widget.destroy()

    def mostrar_inicio(self):
        # Muestra el estado inicial de la interfaz principal.
        self.limpiar_contenido()

        assert self.contenido is not None

        tk.Label(
            self.contenido,
            text="Panel principal",
            bg=self.color_fondo,
            fg=self.color_encabezado,
            font=("Arial", 18, "bold"),
        ).pack(anchor="w", pady=(0, 8))

        tk.Label(
            self.contenido,
            text="Seleccione una opcion superior para visualizar la informacion cargada.",
            bg=self.color_fondo,
            fg=self.color_texto,
            font=("Arial", 12),
        ).pack(anchor="w")

    def mostrar_productos(self):
        # Solicita los productos al servicio y los muestra en pantalla.
        self.limpiar_contenido()

        assert self.contenido is not None

        self.crear_nombre_seccion("Productos registrados")

        for producto in self.restaurante_servicio.listar_productos():
            texto = f"{producto.codigo} - {producto.nombre} | {producto.precio}"
            self.crear_fila_informacion(texto)

    def mostrar_usuarios(self):
        # Solicita los usuarios al servicio y los muestra en pantalla.
        self.limpiar_contenido()

        assert self.contenido is not None

        self.crear_nombre_seccion("Usuarios registrados")

        for usuario in self.restaurante_servicio.listar_usuarios():
            texto = f"{usuario.identificador} - {usuario.nombre} | usuario: {usuario.usuario}"
            self.crear_fila_informacion(texto)

    def crear_nombre_seccion(self, texto):
        # Presenta el titulo de la seccion seleccionada.
        assert self.contenido is not None

        tk.Label(
            self.contenido,
            text=texto,
            bg=self.color_fondo,
            fg=self.color_encabezado,
            font=("Arial", 17, "bold"),
        ).pack(anchor="w", pady=(0, 14))

    def crear_fila_informacion(self, texto):
        # Muestra una fila simple sin crear tablas avanzadas.
        assert self.contenido is not None

        fila = tk.Frame(self.contenido, bg="#ffffff", padx=14, pady=10)
        fila.pack(fill="x", pady=(0, 8))

        tk.Label(
            fila,
            text=texto,
            bg="#ffffff",
            fg=self.color_texto,
            font=("Arial", 11),
        ).pack(anchor="w")

    def crear_barra_estado(self):
        # Muestra una barra inferior con el estado general del sistema.
        barra_estado = tk.Frame(self, bg=self.color_secundario, padx=18, pady=8)
        barra_estado.pack(fill="x", side="bottom")

        tk.Label(
            barra_estado,
            text=(
                f"Productos: {self.restaurante_servicio.cantidad_productos()} | "
                f"Usuarios: {self.restaurante_servicio.cantidad_usuarios()} | "
                "Datos JSON locales"
            ),
            bg=self.color_secundario,
            fg=self.color_texto,
            font=("Arial", 10),
        ).pack(side="left")

    def mostrar_funcionalidad_pendiente(self):
        messagebox.showinfo(
            "Proximamente",
            "Funcionalidad que sera incorporada posteriormente.",
        )

    def cerrar_sesion(self):
        # Regresa al login sin crear otra ventana ni otro mainloop.
        self.al_cerrar_sesion()
