def version_1():
    print("Versión 1 seleccionada.")
    # Aquí va la funcionalidad de la versión 1

def version_2():
    print("Versión 2 seleccionada.")
    # Aquí va la funcionalidad de la versión 2

def version_3():
    print("Versión 3 seleccionada.")
    # Aquí va la funcionalidad de la versión 3

def version_4():
    print("Versión 4 seleccionada.")
    distancia = float(input("Ingrese la distancia del viaje en kilómetros: "))
    numero_pasajeros = int(input("Ingrese el número de pasajeros: "))
    costo_por_kilometro = 0.1  # Costo por kilómetro en dólares
    costo_total = distancia * costo_por_kilometro * numero_pasajeros
    print(f"El costo total del viaje para {numero_pasajeros} pasajeros es de ${costo_total:.2f}.")

def main():
    print("Bienvenido al programa con múltiples versiones.")
    print("Por favor, elija una opción:")
    print("1. Versión 1")
    print("2. Versión 2")
    print("3. Versión 3")
    print("4. Versión 4")
    opcion = input("Ingrese el número de la versión que desea ejecutar: ")

    if opcion == '1':
        version_1()
    elif opcion == '2':
        version_2()
    elif opcion == '3':
        version_3()
    elif opcion == '4':
        version_4()
    else:
        print("Opción inválida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()