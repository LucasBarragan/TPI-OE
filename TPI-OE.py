import csv

# carga de proveedores

def cargar_proveedores():
    try:
        with open("proveedores.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            return list(lector)

    except FileNotFoundError:
        print("Error: No se encontró el archivo de proveedores.")
        return []

# Consultar proveedor (1)

def consultar_proveedor(proveedores):
    cuit_buscado = input("Ingrese el CUIT: ").strip()

    if cuit_buscado == "":
        print("Error: Debe ingresar un CUIT.")
        return

    for proveedor in proveedores:
        if proveedor["cuit"] == cuit_buscado:
            print("\n=== PROVEEDOR ENCONTRADO ===")
            print("CUIT:", proveedor["cuit"])
            print("Razón social:", proveedor["razon_social"])
            print("Rubro:", proveedor["rubro"])
            print("Email:", proveedor["email"])
            print("Teléfono:", proveedor["telefono"])
            return
    print("Proveedor no registrado.")


def registrar_proveedor(proveedores):

    # VALIDACIÓN DE CUIT
    while True:
        cuit = input("Ingrese el CUIT (11 números): ").strip()

        if cuit == "":
            print("Error: Debe ingresar un CUIT.")
            continue

        if not cuit.isdigit():
            print("Error: El CUIT debe contener solo números.")
            continue

        if len(cuit) != 11:
            print("Error: El CUIT debe tener exactamente 11 números.")
            continue

        break

    # VERIFICAR SI YA EXISTE
    for proveedor in proveedores:
        if proveedor["cuit"] == cuit:
            print("El proveedor ya se encuentra registrado.")
            return

    # RAZÓN SOCIAL
    while True:
        razon_social = input("Ingrese la razón social: ").strip()

        if razon_social == "":
            print("Error: Debe ingresar una razón social.")
        else:
            break

    # RUBRO
    while True:
        rubro = input("Ingrese el rubro: ").strip()

        if rubro == "":
            print("Error: Debe ingresar un rubro.")
        else:
            break

    # EMAIL
    while True:
        email = input("Ingrese el email: ").strip()

        if email == "":
            print("Error: Debe ingresar un email.")
            continue

        if "@" not in email:
            print("Error: Email inválido.")
            continue

        break

    # TELÉFONO
    while True:
        telefono = input("Ingrese el teléfono: ").strip()

        if telefono == "":
            print("Error: Debe ingresar un teléfono.")
            continue

        if not telefono.isdigit():
            print("Error: El teléfono debe contener solo números.")
            continue

        if len(telefono) < 8:
            print("Error: El teléfono debe tener al menos 8 dígitos.")
            continue

        if len(telefono) > 15:
            print("Error: El teléfono no puede superar los 15 dígitos.")
            continue

        break

    nuevo_proveedor = {
        "cuit": cuit,
        "razon_social": razon_social,
        "rubro": rubro,
        "email": email,
        "telefono": telefono
    }

    proveedores.append(nuevo_proveedor)


    print("Proveedor registrado correctamente.")
proveedores = cargar_proveedores()


while True:
    print("\n=== SISTEMA DE PROVEEDORES ===")
    print("1. Consultar proveedor")
    print("2. Registrar proveedor")
    print("3. Mostrar proveedores")
    print("4. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        consultar_proveedor(proveedores)

    elif opcion == "2":
        registrar_proveedor(proveedores)

    elif opcion == "3":
        print("Mostrar proveedores")

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")