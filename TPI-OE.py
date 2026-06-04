import csv

def consultar_proveedor():
    cuit_buscado = input("Ingrese el CUIT: ").strip()
    if cuit_buscado == "":
        print("Error: Debe ingresar un CUIT.")
        return

    try:
        with open("proveedores.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            encontrado = False

            for proveedor in lector:
                if proveedor["cuit"] == cuit_buscado:
                    encontrado = True

                    print("\n=== PROVEEDOR ENCONTRADO ===")
                    print("CUIT:", proveedor["cuit"])
                    print("Razón social:", proveedor["razon_social"])
                    print("Rubro:", proveedor["rubro"])
                    print("Email:", proveedor["email"])
                    print("Teléfono:", proveedor["telefono"])
                    break

            if not encontrado:
                print("Proveedor no registrado.")

    except FileNotFoundError:
        print("Error: No se encontró el archivo de proveedores.")

while True:
    print("\n=== SISTEMA DE PROVEEDORES ===")
    print("1. Consultar proveedor")
    print("2. Registrar proveedor")
    print("3. Mostrar proveedores")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        consultar_proveedor()

    elif opcion == "2":
        print("Registrar proveedor")

    elif opcion == "3":
        print("Mostrar proveedores")

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")