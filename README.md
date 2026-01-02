# Gestor de Tareas en Python

Aplicación  en Python que permite gestionar tareas.
El programa permite añadir tareas, verlas, marcarlas como completadas y eliminarlas.
El proyecto realizado de forma colaborativa entre Daniel y Raul

## Integrantes del equipo

- Daniel Estebaranz Hernando  
- Raúl Marzal Utrilla

## Requisitos previos

- Python 3.x

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/danielEstebaranz/gestor-tareas-equipo-05.git
   cd gestor-tareas-equipo-05

2. Crear el entorno virtual:

python -m venv venv
3. Activar el entorno virtual:

Windows:

venv\Scripts\activate
Linux / macOS:

source venv/bin/activate
4. Instalar dependencias:

pip install -r requirements.txt
# Ejecución del programa
python main.py
# Uso del programa
Al ejecutar el programa se muestra el siguiente menú:

======== GESTOR DE TAREAS ==========
1. Ver tareas
2. Añadir tarea
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir
Ejemplo de salida:

Las tareas se guardan en un fichero tareas.txt que se crea automaticamente
Las tareas completadas se marcan con el símbolo ✔.

Estructura del proyecto
gestor-tareas-equipo-05/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── alumno_a/
│   ├── __init__.py
│   └── funciones.py
│
├── alumno_b/
│   ├── __init__.py
│   └── funciones.py

# El fichero .gitignore incluye correctamente los siguientes elementos:

venv/
__pycache__/
*.pyc
tareas.txt
.idea/
.vscode/
