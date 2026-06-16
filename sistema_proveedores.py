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

def guardar_proveedores(proveedores):
    with open("proveedores.csv", "w", newline="", encoding="utf-8") as archivo:
        campos = [
            "cuit",
            "razon_social",
            "rubro",
            "email",
            "telefono"
        ]

        escritor = csv.DictWriter(archivo,fieldnames=campos)
        escritor.writeheader()
        for proveedor in proveedores:
            escritor.writerow(proveedor)

# CONSULTAR PROVEEDOR (1)
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


# REGISTRAR PROVEEDORES (2)
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
            print("Error: El email debe contener '@'.")
            continue
        if email.count("@") != 1:
            print("Error: El email solo puede tener un '@'.")
            continue

        partes = email.split("@")
        usuario = partes[0]
        dominio = partes[1]

        if usuario == "":
            print("Error: Falta el nombre de usuario antes del '@'.")
            continue
        if dominio == "":
            print("Error: Falta el dominio después del '@'.")
            continue
        if "." not in dominio:
            print("Error: El dominio debe contener un punto.")
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
    guardar_proveedores(proveedores)
    print("Proveedor registrado correctamente.")
proveedores = cargar_proveedores()


# MENU PARA VER PROVEEDORES
def menu_proveedores(proveedores):
    while True:
        print("\n=== PROVEEDORES ===")
        print("1. Ver lista de proveedores")
        print("2. Ver todos los detalles")
        print("3. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_proveedores(proveedores)
        elif opcion == "2":
            mostrar_proveedores(proveedores)
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

# LISTA DE PROVEEDORES (3.1)
def listar_proveedores(proveedores):
    if len(proveedores) == 0:
        print("No hay proveedores registrados.")
        return

    print("\n=== LISTA DE PROVEEDORES ===")

    contador = 1
    for proveedor in proveedores:
        print(f"{contador}. {proveedor['razon_social']} - {proveedor['cuit']}")
        contador += 1

    while True:
        seleccion = input("\nIngrese el número del proveedor para ver sus datos (0 para volver): ")
        if not seleccion.isdigit():
            print("Ingrese un número válido.")
            continue
        seleccion = int(seleccion)

        if seleccion == 0:
            return

        if 1 <= seleccion <= len(proveedores):
            proveedor = proveedores[seleccion - 1]
            print("\n=== PROVEEDOR SELECCIONADO ===")
            print("CUIT:", proveedor["cuit"])
            print("Razón social:", proveedor["razon_social"])
            print("Rubro:", proveedor["rubro"])
            print("Email:", proveedor["email"])
            print("Teléfono:", proveedor["telefono"])
            return
        print("Proveedor inexistente.")

# MOSTRAR PROVEEDORES (3.2)
def mostrar_proveedores(proveedores):
    if len(proveedores) == 0:
        print("No hay proveedores registrados.")
        return
    print("\n=== DETALLE DE TODOS LOS PROVEEDORES ===")

    for proveedor in proveedores:
        print("\n-------------------------")
        print("CUIT:", proveedor["cuit"])
        print("Razón social:", proveedor["razon_social"])
        print("Rubro:", proveedor["rubro"])
        print("Email:", proveedor["email"])
        print("Teléfono:", proveedor["telefono"])

# ELIMINAR PROVEEDORES (4)
def eliminar_proveedor(proveedores):
    if len(proveedores) == 0:
        print("No hay proveedores registrados.")
        return
    cuit = input("Ingrese el CUIT del proveedor a eliminar: ").strip()

    for proveedor in proveedores:
        if proveedor["cuit"] == cuit:
            print("\n=== PROVEEDOR ENCONTRADO ===")
            print("CUIT:", proveedor["cuit"])
            print("Razón social:", proveedor["razon_social"])
            confirmacion = input("¿Desea eliminar este proveedor? (S/N): ").strip().upper()

            if confirmacion == "S":
                proveedores.remove(proveedor)
                guardar_proveedores(proveedores)
                print("Proveedor eliminado correctamente.")
            else:
                print("Operación cancelada.")
            return

    print("Proveedor no encontrado.")

while True:
    print("\n=== SISTEMA DE PROVEEDORES ===")
    print("1. Consultar proveedor")
    print("2. Registrar proveedor")
    print("3. Mostrar proveedores")
    print("4. Eliminar proveedores")
    print("5. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        consultar_proveedor(proveedores)

    elif opcion == "2":
        registrar_proveedor(proveedores)

    elif opcion == "3":
        menu_proveedores(proveedores)

    elif opcion == "4":
        eliminar_proveedor(proveedores)

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")