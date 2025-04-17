asientoComun = 60000
asientoparapiernas = 80000
asientoNoreclinable = 50000
pasaje = []
pasajero = []
destino = []
listado = []
asiento = []
lugarescogido = [
    "(0)Miami beach",
    "(1)Moscow",
    "(2)Brasil",
    "(3)Argentina",
    "(4)Bolivia",
    "(5)EEUU",
]
ubicacionesdisponible = (
    "(0)Miami beach",
    "(1)Moscow",
    "(2)Brasil",
    "(3)Argentina",
    "(4)Bolivia",
    "(5)EEUU",
)
print("-----------------------------------------------------------------------------")


def datospasajero():
    nombre = input("Ingrese su nombre: ")
    print("El rut se debe registrar formato numero y sin guion ni puntos")
    rut = int(input("Ingrese su rut: "))
    pasajero = print(f"Sus datos se han registrado correctamente: ", (nombre, rut))
    print(
        "-------------------------------------------------------------------------------"
    )
    return pasajero


def comprapasajes():
    print("(1) El valor de un asiento común es de $60000")
    print("(2) El valor de un asiento con espacio para piernas es de $80000")
    print("(3) El valor de un asiento no reclinable es de $50000")
    pasaje = int(input("¿Cuántos pasajes va a querer?: "))

    for i in range(pasaje):  # Usamos range para iterar según la cantidad de pasajes
        print(f"Pasaje {i + 1}:")
        print(f"Subtotal: {asientoComun + asientoparapiernas + asientoNoreclinable}")
        subtotal = asientoComun + asientoparapiernas + asientoNoreclinable
        asiento.append(subtotal)  # Agregamos el subtotal a la lista de asientos
        listado.append(asiento)  # Agregamos el asiento al listado


def ubicaciones():
    print(ubicacionesdisponible)
    ir = int(input("Ingrese a donde va a ir: "))
    for i in range(lugarescogido):
        lugarescogido = [i, ir[i]]
        listado.append(lugarescogido)


while True:
    print(
        "(1) Registra pasajero\n"
        "\n(2) Comprar pasajes\n"
        "\n(3) Ver ubicación disponibles\n"
        "\n(4) Ver listado de pasajeros\n"
        "\n(5) Buscar asiento\n"
        "\n(6) Cambiar asiento\n"
        "\n(7) Salir"
    )

    opcion = int(input("\nIngrese una opción: "))

    if opcion == 1:
        datospasajero()

    elif opcion == 2:
        comprapasajes()

    elif opcion == 3:
        ubicaciones()

    elif opcion == 4:
        break
