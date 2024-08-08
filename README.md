# Proyecto de Gestión de Cine

Este proyecto es una API de gestión para un sistema de cine, que incluye funcionalidades para manejar asientos, salas, películas, clientes y horarios. Utiliza FastAPI para la implementación del servidor y MySQL para el almacenamiento de datos.

## Estructura del Proyecto

- **`api/`**: Contiene los modelos de datos utilizados por la API.
  - `modelos.py`: Define los modelos Pydantic para la validación de datos.
  
- **`main/`**: Contiene el código principal de la aplicación y la lógica para interactuar con la base de datos.
  - `data_base_cine.py`: Contiene la clase `conexion_base_datos` que maneja las operaciones de base de datos.
  
- **`src/`**: Contiene el código fuente de la aplicación.
  - `api.py`: Configura y ejecuta la API con FastAPI.
  
- **`static/`**: Contiene los archivos estáticos y el código frontend.
  - `scripts.js`: Scripts JavaScript para interactuar con la API desde el frontend.

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu_usuario/nombre_del_repositorio.git
 

2. Navega al directorio del proyecto:

   ```bash
   cd nombre_del_repositorio
   ```

3. Crea un entorno virtual y activa:

   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

4. Instala las dependencias del proyecto:

   ```bash
   pip install -r requirements.txt
   ```

5. Asegúrate de tener MySQL instalado y configurado. Crea una base de datos llamada `cine` y ajusta las credenciales en `data_base_cine.py` si es necesario.

## Uso

1. Inicia el servidor FastAPI:

   ```bash
   uvicorn src.api:app --host 0.0.0.0 --port 8000
   ```

2. Accede a la API en `http://127.0.0.1:8000`.

3. Los endpoints disponibles son:
   - `POST /crear/asientos/`: Añade un nuevo asiento.
   - `POST /crear/salas/`: Añade una nueva sala.
   - `POST /crear/peliculas/`: Añade una nueva película.
   - `POST /crear/clientes/`: Añade un nuevo cliente.
   - `POST /crear/horarios/`: Añade un nuevo horario.

## Frontend

El proyecto incluye scripts JavaScript para enviar datos al backend desde formularios HTML. Asegúrate de que los formularios tengan los IDs correctos como se espera en los scripts para el correcto funcionamiento.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un _issue_ o envía un _pull request_ si encuentras algún problema o tienes sugerencias para mejorar el proyecto.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

Para más información sobre la configuración y el uso, consulta la documentación en línea o el código fuente del proyecto.

Asegúrate de ajustar las secciones como el nombre del repositorio, la URL, y otros detalles según corresponda a tu proyecto. ¿Hay algo más que te gustaría añadir o modificar?


<h1>Formularios de relleno: </h1>
<br>

![Screenshot 2024-08-05 222719](https://github.com/user-attachments/assets/d22e130b-69f7-4d2d-b1f7-98e294a9903a)
