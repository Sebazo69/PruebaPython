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
    rut = str(input("Ingrese su rut: "))
    pasajero = print(f"Sus datos se han registrado correctamente: ", (nombre, rut))
    print(
        "-------------------------------------------------------------------------------"
    )
    return pasajero


def comprapasajes():
    print("(1)El valor de un asiento comun es de $60000")
    print("(2)El valor de un asiento con espacion para pieres es de $80000")
    print("(3)El valor de un asiento no reclinable es de $50000")
    pasaje = int(input("Cuantos pasajes va a querer: "))
    for i in pasaje:
        print(i, pasaje[i])
        subtotal = asientoComun + asientoparapiernas + asientoNoreclinable
        asiento = [asiento, subtotal]
        listado.append(asiento)


def ubicaciones():
    print(ubicacionesdisponible)
    ir = int(input("Ingrese a donde va a ir: "))
    for i in range(lugarescogido):
        lugarescogido = [i, ir[i]]
        listado.append(lugarescogido)


while True:

    print(
        "(1)registra pasajero\n(2)Comprar pasajes\n(2)Ver ubicacion disponibles\n(3)Ver listado de pasajeros\n(4)Buscar asiento\n(5)Cambiar asiento\n(6)Salir"
    )

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        datospasajero()

    elif opcion == 2:
        comprapasajes()

    elif opcion == 3:
        ubicaciones()

    elif opcion == 4:
        break
