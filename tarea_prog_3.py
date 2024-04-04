def version_1():
    print("Versión 1 seleccionada.")
    # Aquí va la funcionalidad de la versión 1

def version_2():
    print("Versión 2 seleccionada.")
    # Aquí va la funcionalidad de la versión 2

def version_3():
    print("Versión 3 seleccionada.")
    # Aquí va la funcionalidad de la versión 3

def main():
    print("Bienvenido al programa con múltiples versiones.")
    print("Por favor, elija una opción:")
    print("1. Versión 1")
    print("2. Versión 2")
    print("3. Versión 3")
    opcion = input("Ingrese el número de la versión que desea ejecutar: ")

    if opcion == '1':
        version_1()
    elif opcion == '2':
        version_2()
    elif opcion == '3':
        version_3()
    else:
        print("Opción inválida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()