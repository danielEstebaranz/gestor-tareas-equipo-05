from colorama import Fore, Style

def mostrar_menu():
    """Muestra el menú principal y devuelve la opción elegida."""
    print("======== GESTOR DE TAREAS ==========")
    print("1. Ver tareas")
    print("2. Añadir tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("Elige opción: ")
    return opcion
    
def ver_tareas():
    """Muestra todas las tareas numeradas."""
    try:
        with open("tareas.txt", "r", encoding="utf-8") as f:
            lineas = f.readlines()

        if not lineas:
            print(Fore.GREEN + "No hay tareas todavía." + Style.RESET_ALL)
            return

        print("\n=== MIS TAREAS ===")
        numero = 1
        for linea in lineas:
            estado, texto = linea.strip().split("|")
            if estado == "0":
                print(Fore.YELLOW + f"{numero}. [ ] {texto}" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"{numero}. [✓] {texto}" + Style.RESET_ALL)
            numero += 1

    except FileNotFoundError:
        print(Fore.WHITE + "No hay tareas todavía." + Style.RESET_ALL)
    
    
def añadir_tarea():
    """Añade una nueva tarea al fichero."""
    tarea = input("Introduce la nueva tarea: ")

    with open("tareas.txt", "a", encoding="utf-8") as f:
        f.write(f"0|{tarea}\n")

    print(Fore.GREEN + "Tarea añadida correctamente." + Style.RESET_ALL)
    pass