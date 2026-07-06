def cargar_inventario():
    inventario = {}
    with open("productos.txt", "r") as f:
        for linea in f:
            if linea.strip():
                codigo, nombre, precio = linea.strip().split(",")
                inventario[codigo] = {"nombre": nombre, "precio": float(precio)}
    return inventario

def guardar_venta_estadisticas(carrito, total_final):
    with open("estadisticas.txt", "a") as f:
        f.write(f"Venta | Total: ${total_final:.2f} | Productos: ")
        for item in carrito:
            f.write(f"{item['cantidad']}x {item['nombre']}, ")
        f.write("\n")

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
    
    total_final = total_sin_descuento
    if total_final > 15000:
        descuento = total_final * 0.10
        total_final -= descuento
        print(f"¡Promoción aplicada! Descuento 10%: -${descuento:.2f}")
        
    print(f"TOTAL A PAGAR: ${total_final:.2f}")
    print("="*30 + "\n")
    return total_final

def mostrar_estadisticas(total_recaudado, registro_ventas):
    print("\n--- ESTADÍSTICAS DE VENTAS ---")
    print(f"Total ingresos: ${total_recaudado:.2f}")
    
    if not registro_ventas:
        print("Aún no se han vendido productos.")
    else:
        print("Productos vendidos:")
        for nombre, cantidad in registro_ventas.items():
            print(f"- {nombre}: {cantidad} unidades")
    print("------------------------------")

def main():
    inventario = cargar_inventario()
    total_recaudado = 0.0
    registro_ventas = {}
    carrito = []
    total_actual = 0.0

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                print("\nProductos disponibles:")
                for key, prod in inventario.items():
                    print(f"[{key}] {prod['nombre']} - ${prod['precio']:.2f}")
                print("[0] Terminar carga")
                
                seleccion = input("Ingrese el código: ")
                
                if seleccion == "0":
                    break
                
                if seleccion in inventario:
                    try:
                        cantidad = int(input(f"Cantidad de '{inventario[seleccion]['nombre']}': "))
                        if cantidad <= 0:
                            print("Error: Cantidad inválida.")
                            continue
                        
                        subtotal = inventario[seleccion]["precio"] * cantidad
                        total_actual += subtotal
                        
                        carrito.append({
                            "nombre": inventario[seleccion]["nombre"],
                            "cantidad": cantidad,
                            "subtotal": subtotal
                        })
                        print(f"-> Agregado correctamente.")
                        
                    except ValueError:
                        print("Error: Ingrese un número válido.")
                else:
                    print("Error: Código no válido.")

        elif opcion == "2":
            if carrito:
                total_cobrado = generar_ticket(carrito, total_actual)
                total_recaudado += total_cobrado
                guardar_venta_estadisticas(carrito, total_cobrado)
                
                for item in carrito:
                    registro_ventas[item['nombre']] = registro_ventas.get(item['nombre'], 0) + item['cantidad']
                
                carrito.clear()
                total_actual = 0.0
            else:
                print("\nError: Carrito vacío.")

        elif opcion == "3":
            mostrar_estadisticas(total_recaudado, registro_ventas)

        elif opcion == "4":
            print("\nSaliendo...")
            break

        else:
            print("\nError: Opción incorrecta.")

if __name__ == "__main__":
    main()