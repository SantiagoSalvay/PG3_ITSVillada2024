## Projecto Django con API's

Este proyecto es una aplicación Django que muestra una lista de películas utilizando una API externa.

## API Utilizada

Utilizamos la API de [OMDb](http://www.omdbapi.com/), que proporciona información sobre películas, series y episodios de televisión.

### Endpoints Principales

-- **Buscar películas por título**: `http://www.omdbapi.com/?apikey={apikey}&s={titulo}`

## Cómo Trabajamos con la API

1. **Configuración del Proyecto Django**:
    - Creamos primero nuestro entorno virtual
    -  Activamos el entorno virtual y creamos un nuevo proyecto Django y una aplicación dentro de este proyecto.
    - Configuramos las URLs y vistas para manejar las solicitudes y renderizar las plantillas HTML.

2. **Estructura del Proyecto**:
    - `trabajoapi/queri/views.py`: Contiene las vistas que manejan las solicitudes a la API y renderizan las plantillas.
    - `trabajoapi/queri/urls.py`: Define las rutas de la aplicación.
    - `trabajoapi/queri/templates/queri/`: Contiene las plantillas HTML para renderizar las páginas web.

3. **Vistas**:
    - Definimos una vista llamada `movies_view` que realiza una solicitud a la API de OMDb, obtiene una lista de películas y las pasa a la plantilla `movies.html`.
