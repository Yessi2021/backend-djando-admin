# BI360 Backend

This project is a backend developed in Python. We use Poetry to manage the project's dependencies efficiently.

## Prerequisites

Before you begin, make sure you have Python 3.8 or higher and Poetry installed. If you do not have Poetry, you can install it with the following [instructions](https://python-poetry.org/docs/#installing-with-the-official-installer)

_Remember add poetry to path. When you run poetry the console should show such as `Poetry (version 1.2.0)`_

## Setup local

Para configurar el proyecto en tu entorno local, sigue estos pasos:

1. Clonar el Repositorio
   Clona el repositorio del proyecto a tu máquina local usando:

```
git clone ###backend-py-bi360.git.git
```

2. Dirijete a la carpeta del proyecto

```
cd backend-py-bi360
```

3. Create the Database
   Create an empty database using PostgreSQL v.13 or higher

4. Create a `.env` file at the root of the project and add the necessary environment variables. An example is:

```
DEBUG=on
SECRET_KEY=key
DB_USER=postgres
DB_PORT=5432

DB_HOST=localhost
DB_NAME=bi360
DB_PASS='pass'

EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='mail@to_use.com'
EMAIL_HOST_PASSWORD='pass'
```

5. Instalación de Dependencias
   _Make sure that your database service is running and then perform the migrations_

Inside the project directory, execute:

```
make update
```

This command will install all the necessary dependencies for the project, apply the migrations, and the pre-commit.

6. To run the dev server, exec

```
make run-server
```

Starting development server at http://localhost:8000.
