
acciones = []

def registrar_accion(descripcion):
    acciones.append(descripcion)
    print("Acción registrada:", descripcion)

def deshacer():
    if not acciones:
        print("No existen acciones para deshacer")
        return

    ultima = acciones.pop()
    print("Se deshizo:", ultima)

def historial():
    if not acciones:
        print("No hay acciones pendientes")
    else:
        print("\nAcciones pendientes:")

        for accion in reversed(acciones):
            print("-", accion)

while True:
    print("\n--- Menú de acciones ---")
    print("1. Registrar acción")
    print("2. Deshacer última acción")
    print("3. Mostrar historial")
    print("4. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        descripcion = input("Ingrese la descripción de la acción: ").strip()

        if descripcion:
            registrar_accion(descripcion)
        else:
            print("Error: la descripción no puede estar vacía")

    elif opcion == "2":
        deshacer()

    elif opcion == "3":
        historial()

    elif opcion == "4":
        print("Programa finalizado")
        break

    else:
        print("Opción no válida. Ingrese un número del 1 al 4.")
