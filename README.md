# Fundamentos de interfaces graficas de usuario con Tkinter

## Tema

Fundamentos de interfaces graficas de usuario con Tkinter.

## Objetivo de aprendizaje

Comprender como una aplicacion de consola puede incorporar una interfaz grafica sin reemplazar su arquitectura. La GUI se encarga de la presentacion y de los eventos, mientras que los servicios conservan la logica del sistema y el acceso a los datos.

## Evolucion del programa

ANTES

Usuario -> CLI -> Servicios -> Modelos -> JSON

AHORA

Usuario -> GUI -> Eventos -> Servicios -> Modelos -> JSON

## Capas del proyecto

`modelos/`: clases sencillas que representan la informacion del sistema, como usuarios y productos.
Tambien aplican validaciones basicas con `property` para evitar objetos con datos obligatorios vacios.

`servicios/`: clases que contienen la logica de negocio y el acceso a los archivos JSON.

`datos/`: archivos JSON con informacion persistente de ejemplo.

`ui/`: vistas graficas creadas con Tkinter para interactuar con el usuario.

`main.py`: punto de entrada que inicializa los servicios, muestra la primera vista y ejecuta la aplicacion.

## Componentes Tkinter utilizados

`Tk`: crea la ventana principal de la aplicacion.

`Label`: muestra textos dentro de la interfaz.

`Entry`: permite ingresar datos como usuario y contrasena.

`Button`: ejecuta una accion cuando el usuario hace clic.

`messagebox`: muestra mensajes emergentes simples.

`ttk.Style`: permite definir estilos reutilizables para algunos componentes visuales.

## Concepto de evento

Usuario hace clic -> Button genera una accion -> command ejecuta un metodo -> el metodo consulta el servicio -> la interfaz muestra el resultado.

En el login, el boton usa `command=self.iniciar_sesion`. Ese metodo obtiene los datos escritos, valida campos vacios y solicita al servicio la verificacion de credenciales.

## Funcionamiento del proyecto

Inicio -> Login -> Validacion -> Interfaz principal -> Cerrar sesion -> Login

La interfaz principal muestra una barra superior con opciones visuales. Las secciones de libros y usuarios permiten listar informacion cargada desde JSON. Las operaciones de prestamos y ventas todavia no estan implementadas.

La pantalla central cambia su contenido cuando el usuario selecciona una opcion superior. Esto permite visualizar el concepto de evento sin construir todavia formularios ni operaciones CRUD.

## Persistencia JSON

La persistencia JSON desarrollada previamente continua funcionando. Los usuarios y libros se cargan desde archivos locales al iniciar la aplicacion.

La GUI no reemplaza los servicios ni los modelos. La interfaz solicita operaciones al servicio, y el servicio trabaja con los modelos y los datos persistidos.

Los modelos usan constructores tradicionales con `__init__` y validaciones con `property`, de modo que el paso de diccionarios JSON a objetos sea facil de seguir durante la explicacion.

## Requisitos

- Python 3.x
- Tkinter disponible en la instalacion de Python

No se requieren dependencias externas.

## Como ejecutar

Desde la carpeta del proyecto:

```bash
python main.py
```

En Windows, si el comando `python` no esta disponible en la terminal, puede usarse:

```bash
py main.py
```

## Credenciales de demostracion

Se crearon 4 usuarios diferentes para probar la eficiencia del programa
Siendo el primer usuario Edison Moyano
Usuario: `admin`

Contrasena: `1234`



## Nota educativa sobre autenticacion

La autenticacion de este proyecto es local y simulada. Las contrasenas se guardan en JSON solo para fines pedagogicos. En una aplicacion real, almacenar contrasenas de esta forma no seria apropiado ni seguro.

## Proxima evolucion

En las siguientes practicas se profundizara en componentes y contenedores para construir las operaciones reales de la aplicacion.

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
├── main.py
└── README.md