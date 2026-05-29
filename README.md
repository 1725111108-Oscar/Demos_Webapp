# Demo de Webapp con python3, Web.py y Sqlite3

## 1. Crear un Ambiente Virtual (Virtual Enviroment)

````shell
python3 -m venv .venv
````



## 2. Iniciar el Virtual Enviroment

Iniciar el virtual enviroment para instalar las librerias necesarias para el proyecto

````shell
source .venv/bin/activate
````

## 3. Actualizar el instalador de paquetes de Python **pip**


````shell
pip install --upgrate pip
````


## 4.instalar el micro--framework **web.py**

Instalar el micro-framework **web.py** para la creacion de Aplicaciones Web utilizando python

````shell
pip install web.py
````

## 5. Crear el archivo **requirement.txt**

Crear el archivo **requirement.txt** con la lista de las librerias y versiones de cada una, necesarias para el proyecto.

````shell
pip freeze > requirements.txt
````



## 6. Crear el archivo **rinetime.txt** con la version de Python 3 utilizada.

````shell
python3 -V > runetime.txt
````

## 7. Crear el archivo **.gitignore**

Crear el archivo **.gitignore** para indicar las carpetas y archivos que no se van a sincronizar con el repositorio.

````shell
*.pyc
__pycache__/
.venv/
````

## 8. Indexar las carpetas y archivos 

Indexar las carpetas y archivos creados o modificados

````shell
git add .
````

## 9. Crear el punto de control **commit**

Crear el punto de control con los cambios realizados al proyecto.

````shell
git commit -m "CREATED configuracion del virtual enviroment"
````

## 10. Sincronizar los cambios al repositorio

Sincronizar los cambios realizados al proyecto con el repositorio

````shell
git push -u origin main 
````
