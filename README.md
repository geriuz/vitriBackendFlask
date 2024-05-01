# Vitrina Web CBC API Rest FLask

Aplicación API Rest CRUD Tienda online usuando [Flask](http://flask.pocoo.org), [SQLAlchemy](http://www.sqlalchemy.org) & [Marshmellow](https://flask-marshmallow.readthedocs.io/en/latest/), y la conexión de ambos usando la libreria [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org).

## Empezando
1. **Obtener el código fuente del proyecto** 

Haga esto clonando el repositorio [VitriBackendFlask](https://github.com/geriuz/VitriBackendFlask).
```
git clone https://github.com/geriuz/VitriBackendFlask
cd VitriBackendFlask
```

2. **Crear un entorno virtual para el proyecto e instalar las dependecias**
```
python -m venv venv
```
3. **Activar el entorno virtual**

Sistema Operativo|Comando
:-:|:-:|
Windows|`venv/Scripts/activate`
Linux|`source .venv/bin/activate`

 > _Es posible que en Windows se encuentre con el siguiente error al intentar ejecutar el script `venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies`_

Para solucionar esto, puedes utilizar la política de ejecución de conjuntos para permitir que el usuario actual ejecute scripts de la siguiente manera

```
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```

4. **Instalar las dependencias**
```
pip install -r requirements.txt
```

5. **Crear un nuevo archivo de entorno (.env) en la raiz del proyecto y configurarlo**

Sistema Operativo|Comando
:-:|:-:|
Windows|`New-Item ".env" -ItemType File`
Linux|`touch .env`

* Contenido y configuración del archivo .env
```
DEBUG=TRUE
SQLALCHEMY_DATABASE_URI='mysql://root:1234@localhost/vitrinadb'
SQLALCHEMY_TRACK_MODIFICATIONS=FALSE
```

Actualizar `SQLALCHEMY_DATABASE_URI` en el archivo `.env` de acuerdo a la información de tu base de datos MySQL


## Correr la aplicación

### 1) Con Database Migration

* **Establecer la variable de entorno FLASK_APP en el valor app.py**

> _Esto es útil porque permite iniciar la aplicación Flask sin tener que especificar explícitamente el nombre del archivo o el módulo de la aplicación cada vez_

Sistema Operativo|Terminal| Comando
:-:|:-:|:-:|
Windows|Powershell|`$env:FLASK_APP="app.py"`
Windows|CMD|`set FLASK_APP=app.py`
Linux|Bash|`export FLASK_APP=app.py`

* **Inicializar la extensión Flask-Migrate dentro de la aplicación Flask**

```
flask db init
```

* **Crear archivo de migración para todas las tablas**
```
flask db migrate -m tables
```

* **Actualizar la base de datos con el archivo de migración previamente creado**
```
flask db upgrade
```

* **Correr o inicializar la aplicación**
```
flask run --debug
```
> _La aplicación iniciará en la siguiente URL: http://localhost:5000 en modo desarrollo (DEBUG), si deseas iniciar la aplicación con el modo desarrollador (DEBUG) desactivado solo debes omitir la opción `--debug` del comando_

* **Cambiar puerto en el que se inicia la aplicación al utilizar el comando `"flask run"`**

Sistema Operativo|Terminal| Comando
:-:|:-:|:-:|
Windows|Powershell|`$env:FLASK_RUN_PORT = 8087`
Windows|CMD|`set FLASK_RUN_PORT=8087`
Linux|Bash|`export FLASK_RUN_PORT=8000`

Al ejecutar el comando `flask run --debug` la aplicación iniciará en el puerto establecido `8087` la URL quedara se la siguiente forma: http://localhost:8087, si deseas que se inicie en otro puerto solo debes especificarlo en el comando.

### 2) Sin Migration

Debes correr el siguiente comando, creará las tablas de la base de datos e inciará el proyecto en la siguiente URL: http://localhost:8087 y el modo de desarrollo (DEBUG) estará encendido (ON)

```
python app.py
```
Si quieres cambiar el puerto ve al archivo [app.py](https://github.com/geriuz/VitriBackendFlask/blob/main/app.py) ubicado en la raiz del proyecto y edita la siguiente linea de código:
```
app.run(debug=True, port=8087)
```
