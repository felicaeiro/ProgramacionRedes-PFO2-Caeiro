# Propuesta Formativa Obligatoria - Programación sobre Redes
## Felicitas Caeiro
**Tecnicatura Superior en Desarrollo de Software - IFTS N° 29**

# Sistema de Gestión de Tareas con API y Base de Datos

Este proyecto es una API con Flask que permite registrar usuarios, iniciar sesión y gestionar tareas básicas.

## Requisitos

- Python 3.8+ instalado

## Instalación

1. Abre una terminal en la carpeta del proyecto:

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar el servidor

1. Asegúrate de que el entorno virtual está activado.
2. Ejecuta el servidor Flask:

```bash
python servidor.py
```

El servidor quedará disponible en:

```text
http://127.0.0.1:5000
```

## Probar el proyecto

### Usar el cliente interactivo

Ejecuta el cliente de prueba:

```bash
python cliente.py
```

El cliente ofrece un menú para:

- Registrar un usuario
- Iniciar sesión
- Ver los usuarios registrados a través de la API

### Endpoints disponibles

- `POST /registro` — Registrarse con JSON `{ "usuario": "<nombre>", "contraseña": "<clave>" }`
- `POST /login` — Iniciar sesión con JSON `{ "usuario": "<nombre>", "contraseña": "<clave>" }`
- `GET /usuarios` — Obtener la lista de usuarios registrados (solo `id` y `usuario`)
- `GET /tareas` — Página web interactiva con un único formulario para registro y login. El formulario usa dos botones distintos para enviar a `/registro` o `/login`.

## Base de datos

El proyecto usa SQLite y crea el archivo `chat.db` automáticamente al iniciar el servidor.

## Archivos importantes

- `servidor.py` — Punto de entrada del servidor Flask
- `cliente.py` — Cliente de consola para probar registro y login
- `database.py` — Conexión y creación de tablas SQLite
- `routes/auth_routes.py` — Rutas de autenticación y usuarios
- `routes/tareas_routes.py` — Ruta de tareas

## Notas

- La ruta `GET /usuarios` devuelve solo `id` y `usuario`, sin exponer contraseñas.

## Tecnologías usadas

- Python 3.8+
- Flask
- SQLite
- `requests` para el cliente
- `werkzeug.security` para el hashing de contraseñas
