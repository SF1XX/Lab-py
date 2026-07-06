def mostrar_menu():
    print("\n--- SISTEMA DE CAJA: SUPERMERCADO ---")
    print("1. Agregar producto al carrito")
    print("2. Generar ticket y cobrar")
    print("3. Ver estadísticas de ventas")
    print("4. Salir")
    print("-------------------------------------")

def generar_ticket(carrito, total_sin_descuento):
    print("\n" + "="*30)
    print("          TICKET DE COMPRA          ")
    print("="*30)
    for item in carrito:
        print(f"{item['cantidad']}x {item['nombre']} - ${item['subtotal']:.2f}")
    print("-" * 30)
    print(f"TOTAL A PAGAR: ${total_sin_descuento:.2f}")
    print("="*30 + "\n")
    return total_sin_descuento

def main():
    inventario = {
        "1": {"nombre": "Yogur Tregar", "precio": 1200},
        "2": {"nombre": "Fiambre Paladini", "precio": 3500},
        "3": {"nombre": "Pechuga de Pollo (1kg)", "precio": 6500},
        "4": {"nombre": "Huevos (Docena)", "precio": 2200}
    }
    
    carrito = []
    total_actual = 0.0

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                print("\nProductos disponibles:")
                for key, prod in inventario.items():
                    print(f"[{key}] {prod['nombre']} - ${prod['precio']}")
                print("[0] Terminar carga de productos")
                
                seleccion = input("Ingrese el código del producto: ")
                
                if seleccion == "0":
                    break
                elif seleccion in inventario:
                    try:
                        cantidad = int(input(f"Ingrese la cantidad de '{inventario[seleccion]['nombre']}': "))
                        if cantidad <= 0:
                            print("Error: La cantidad debe ser mayor a cero.")
                            continue
                        
                        subtotal = inventario[seleccion]["precio"] * cantidad
                        total_actual += subtotal
                        
                        carrito.append({
                            "nombre": inventario[seleccion]["nombre"],
                            "cantidad": cantidad,
                            "subtotal": subtotal
                        })
                        
                        print(f"-> {cantidad}x {inventario[seleccion]['nombre']} agregado(s) correctamente.")
                        
                    except ValueError:
                        print("Error: Por favor, ingrese un número entero válido.")
                else:
                    print("Error: Código de producto no válido.")

        elif opcion == "2":
            if len(carrito) > 0:
                generar_ticket(carrito, total_actual)
                carrito = []
                total_actual = 0.0
            else:
                print("\nError: Debe agregar productos al carrito primero (Opción 1).")

        elif opcion == "3":
            print("\nEn desarrollo...")
        elif opcion == "4":
            print("\nSaliendo del sistema de caja... ¡Hasta luego!")
            break
        else:
            print("\nError: Opción incorrecta. Intente nuevamente.")

if __name__ == "__main__":
    main()