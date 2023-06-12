instructores = {}


def agregar_modificar():
    nombre = input("Ingrese el nombre del instructor: ")
    if nombre in instructores:
        print("Nombre: ", nombre)
        print("Materia: ", instructores[nombre]["materia"])
        print("Teléfono: ", instructores[nombre]["telefono"])
        modificar = input("¿Desea modificar los datos? (S/N): ")
        if modificar.lower() == "s":
            materia = input("Ingrese la nueva materia: ")
            telefono = input("Ingrese el nuevo teléfono: ")
            instructores[nombre]["materia"] = materia
            instructores[nombre]["telefono"] = telefono
            print("Datos modificados correctamente.")
    else:
        materia = input("Ingrese la materia: ")
        telefono = input("Ingrese el teléfono: ")
        instructores[nombre] = {"materia": materia, "telefono": telefono}
        print("Instructor agregado correctamente.")

def buscar():
    busqueda = input("Ingrese  búsqueda: ")
    resultados = [nombre for nombre in agenda.keys() if nombre.startswith(busqueda)]
    if len(resultados) > 0:
        print("Resultados:")
        for nombre in resultados:
            print("Nombre: ", nombre)
            print("Materia: ", instructores[nombre]["materia"])
            print("Teléfono: ", instructores[nombre]["telefono"])
    else:
        print("No se encontraron resultados.")

def borrar():
    nombre = input("Ingrese el nombre del instructor a borrar: ")
    if nombre in instructores:
        confirmacion = input("¿Está seguro de que desea borrar a este instructor? (S/N): ")
        if confirmacion == "s" or "S":
            del agenda[nombre]
            print("Instructor borrado correctamente.")
        else:
            print("No se borro.")
    else:
        print("El instructor no se encuentra en la ficha.")

def listar():
    print("Lista de instructores:")
    for nombre in instructores():
        print("Nombre: ", nombre)
        print("Materia: ", instructores[nombre]["materia"])
        print("Teléfono: ", instructores[nombre]["telefono"])

while True:
    print("------ Agenda de Instructores ------")
    print("1. Agregar/Modificar instructor")
    print("2. Buscar instructor")
    print("3. Borrar instructor")
    print("4. Listar instructores")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        agregar_modificar()
    elif opcion == "2":
        buscar()
    elif opcion == "3":
        borrar()
    elif opcion == "4":
        listar()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese nuevamente.")