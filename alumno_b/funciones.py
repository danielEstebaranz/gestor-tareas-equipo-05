from colorama import Fore, Style

def marcar_completada():
    try:
        with open("tareas.txt", "r") as f:
            tareas = f.readlines()

        if not tareas:
            print(Fore.YELLOW + "No hay tareas" + Style.RESET_ALL)
            return

        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea.strip()}")

        num = int(input("Numero de la tarea completada: "))
        tareas[num - 1] = tareas[num - 1].strip() + " ✔\n"

        with open("tareas.txt", "w") as f:
            f.writelines(tareas)

        print(Fore.GREEN + "Tarea marcada como completada " + Style.RESET_ALL)

    except:
        print(Fore.RED + "Error al marcar la tarea" + Style.RESET_ALL)


def eliminar_tarea():
    try:
        with open("tareas.txt", "r") as f:
            tareas = f.readlines()

        if not tareas:
            print(Fore.YELLOW + "No existen tareas" + Style.RESET_ALL)
            return

        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea.strip()}")

        num = int(input("Numero de la tarea para eliminar: "))
        tareas.pop(num - 1)

        with open("tareas.txt", "w") as f:
            f.writelines(tareas)

        print(Fore.GREEN + "Tarea eliminada" + Style.RESET_ALL)
    except:
        print(Fore.RED + "Error al eliminar la tarea" + Style.RESET_ALL)


def despedida():
    print(Fore.BLUE + "Saliendo ...." + Style.RESET_ALL)