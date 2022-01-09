# inegi-test

##### Realizar lo siguiente utilizando servicios serverless

Crear un servicio que proporcione la información de los negocios por localidades (Municipio/Delegación) del INEGI.  

###### Tareas
- Consultar la información del INEGI.
- Proporcionar un endpoint donde poder consultar la información por una o varios municipios o delegaciones.
- Realizar fork del repositorio y solicitar pull request de la solución.
- Opcionales:
    - Pruebas unitarias


## Solución

### Requerimientos
- Docker 4.1.1
- Python 3.7 o superior
- SMBD (pgAdmin4)


### Endpoint

Zappa  
- <zappa_url>/entidades/listar/<entidad_federativa>/<municipio>/<nombre_establecimiento>/

Docker 
- localhost:9001/entidades/listar/<entidad_federativa>/<municipio>/<nombre_establecimiento>/
```

Donde:
    zappa_url: es la url generada al hacer deploy
    entidad_federativa: Clave de dos dígitos de la entidad federativa (01 a 32). Para incluir todas las entidades se especifica 00.
    municipio: Clave de tres dígitos del municipio (ej. 001). Para incluir todos los municipios se especifica 0.
    nombre_establecimiento: Nombre del establecimiento a buscar (ej. oxxo).
```

### Set up con Docker

Ejecutar el siguiente comando desde una terminal:  
`docker-compose build`  

Levantar el contenedor:  
`docker-compose up`

### Set up Serverless con Zappa

Crear o activar ambiente virtual:
- Crear ambiente virtual:
    `python3 -m venv <nombre_ambiente>`

- Activar ambiente virtual:
    `source <nombre_ambiente>/bin/activate`

- Desactivar ambiente virtual:
    `deactivate`

Instar requerimientos:  
`pip3 install -r requirements.txt`

Deploy de la app:
`zappa deploy dev`
