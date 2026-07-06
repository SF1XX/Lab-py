def mostrar_menu():
    print("\n--- SISTEMA DE CAJA: SUPERMERCADO ---")
    print("1. Agregar producto al carrito")
    print("2. Generar ticket y cobrar")
    print("3. Ver estadísticas de ventas")
    print("4. Salir")
    print("-------------------------------------")

def main():
    inventario = {
        "1": {"nombre": "Yogur Tregar", "precio": 1200},
        "2": {"nombre": "Fiambre Paladini", "precio": 3500},
        "3": {"nombre": "Pechuga de Pollo (1kg)", "precio": 6500},
        "4": {"nombre": "Huevos (Docena)", "precio": 2200}
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nEn desarrollo...")
        elif opcion == "2":
            print("\nEn desarrollo...")
        elif opcion == "3":
            print("\nEn desarrollo...")
        elif opcion == "4":
            print("\nSaliendo del sistema de caja... ¡Hasta luego!")
            break
        else:
            print("\nError: Opción incorrecta. Intente nuevamente.")

if __name__ == "__main__":
    main()