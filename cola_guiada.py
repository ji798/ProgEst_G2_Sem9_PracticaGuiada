
from collections import deque
#dque es una estructura de datos que permite agregar y quitar elementos tanto del principio como del final de una colección.

cola = deque()

def registrar_paciente(nombre):
    nombre = nombre.strip()

    if not nombre:
        print("Error: el nombre no puede estar vacío")
        return

    cola.append(nombre)
    print(f"Registrado: {nombre}")

def atender_paciente():
    if not cola:
        print("No hay pacientes en espera")
    else:
        paciente = cola.popleft()
        print(f"Atendiendo a: {paciente}")

def mostrar_cola():
    if not cola:
        print("La cola está vacía")
    else:
        print("Pacientes en espera:")

        for posicion, paciente in enumerate(cola, 1):
            print(f"{posicion}. {paciente}")

"""Respuestas:
# 1 La diferencia entre pop() y popleft() es que pop()
# elimina el último elemento de una lista, mientras
# que popleft() elimina el primer elemento de un deque.
#
# 2 Si se utilizara una pila para atender pacientes, se
# atendería primero al último paciente registrado."""

while True:
    print("Sistema de atención de pacientes")
    print("1. Registrar paciente")
    print("2. Atender paciente")
    print("3. Mostrar pacientes en espera")
    print("4. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        nombre = input("Ingrese el nombre del paciente: ")
        registrar_paciente(nombre)

    elif opcion == "2":
        atender_paciente()

    elif opcion == "3":
        mostrar_cola()

    elif opcion == "4":
        print("Sistema finalizado")
        break

    else:
        print("Opción no válida. Ingrese un número del 1 al 4.")
