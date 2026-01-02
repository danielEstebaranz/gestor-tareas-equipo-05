from colorama import init
from alumno_a.funciones import mostrar_menu, ver_tareas, añadir_tarea
from alumno_b.funciones import marcar_completada, eliminar_tarea, despedida


while True:
    mostrar_menu()
    opcion = input("Elige opción: ")

    if opcion == "1":
        ver_tareas()
    elif opcion == "2":
        añadir_tarea()
    elif opcion == "3":
        marcar_completada()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        despedida()
        break
    else:
        print("Opción no válida")
