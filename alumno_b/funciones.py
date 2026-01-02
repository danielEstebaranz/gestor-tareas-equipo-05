from colorama import Fore, Style

def marcar_completada():
    try:
        with open("tareas.txt", "r", encoding="utf-8") as f:
            tareas = f.readlines()

        if not tareas:
            print(Fore.YELLOW + "No hay tareas" + Style.RESET_ALL)
            return

        print("=== MIS TAREAS ===")
        for i in range(len(tareas)):
            print(f"{i+1}. {tareas[i].strip()}")

        num = input("Numero de la tarea completada: ")

        if not num.isdigit():
            print(Fore.RED + "Debes introducir un número" + Style.RESET_ALL)
            return

        num = int(num) - 1

        if num < 0 or num >= len(tareas):
            print(Fore.RED + "Número fuera de rango" + Style.RESET_ALL)
            return

        if "✔" not in tareas[num]:
            tareas[num] = tareas[num].strip() + " ✔\n"

        with open("tareas.txt", "w", encoding="utf-8") as f:
            f.writelines(tareas)

        print(Fore.GREEN + "Tarea marcada como completada" + Style.RESET_ALL)

    except FileNotFoundError:
        print(Fore.YELLOW + "No hay tareas todavía" + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + "Error al marcar la tarea" + Style.RESET_ALL)

def eliminar_tarea():
    try:
        with open("tareas.txt", "r") as f:
            tareas = f.readlines()

        if not tareas:
            print(Fore.YELLOW + "No existen tareas" + Style.RESET_ALL)
            return

        i = 1
        for tarea in tareas:
            print(str(i) + ". " + tarea.strip())
            i += 1

        num = int(input("Numero de la tarea para eliminar: "))
        tareas.pop(num - 1)

        with open("tareas.txt", "w") as f:
            f.writelines(tareas)

        print(Fore.GREEN + "Tarea eliminada" + Style.RESET_ALL)

    except:
        print(Fore.RED + "Error al eliminar la tarea" + Style.RESET_ALL)



def despedida():
    print(Fore.BLUE + "Saliendo ...." + Style.RESET_ALL)



