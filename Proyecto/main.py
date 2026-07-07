# Umbral y porcentaje de descuento por compras grandes
UMBRAL_DESCUENTO = 15000
PORCENTAJE_DESCUENTO = 0.10

def cargar_inventario():
    inventario = {}
    try:
        # Abre el archivo en modo lectura ("r")
        with open("productos.txt", "r") as f:
            for linea in f:
                # Ignora líneas en blanco
                if linea.strip():
                    # Separa el código, nombre y precio usando la coma
                    codigo, nombre, precio = linea.strip().split(",")
                    inventario[codigo] = {"nombre": nombre, "precio": float(precio)}
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'productos.txt'. El inventario quedará vacío.")
    return inventario

def guardar_venta_estadisticas(carrito, total_final):
    # Abre el archivo en modo "append" ("a") para no borrar lo anterior
    with open("estadisticas.txt", "a") as f:
        f.write(f"Venta | Total: ${total_final:.2f} | Productos: ")
        for item in carrito:
            f.write(f"{item['cantidad']}x {item['nombre']}, ")
        f.write("\n")

def mostrar_menu():
    # Imprime las opciones principales del sistema
    print("\n--- SISTEMA DE CAJA: SUPERMERCADO ---")
    print("1. Agregar producto al carrito")
    print("2. Generar ticket y cobrar")
    print("3. Ver estadísticas de ventas")
    print("4. Salir")
    print("-------------------------------------")

def generar_ticket(carrito, total_sin_descuento):
    # Imprime el encabezado del ticket
    print("\n" + "="*30)
    print("          TICKET DE COMPRA          ")
    print("="*30)

    # Recorre el carrito e imprime cada producto
    for item in carrito:
        print(f"{item['cantidad']}x {item['nombre']} - ${item['subtotal']:.2f}")
    print("-" * 30)
    
    total_final = total_sin_descuento
    if total_final > UMBRAL_DESCUENTO:   # Aplica descuento si supera el umbral
        descuento = total_final * PORCENTAJE_DESCUENTO
        total_final -= descuento
        print(f"¡Promoción aplicada! Descuento {int(PORCENTAJE_DESCUENTO*100)}%: -${descuento:.2f}")
        
    print(f"TOTAL A PAGAR: ${total_final:.2f}")
    print("="*30 + "\n")
    return total_final

def mostrar_estadisticas(total_recaudado, registro_ventas):
    print("\n--- ESTADÍSTICAS DE VENTAS ---")
    print(f"Total ingresos: ${total_recaudado:.2f}")
    
    # Verifica si el diccionario de ventas está vacío
    if not registro_ventas:
        print("Aún no se han vendido productos.")
    else:
        print("Productos vendidos:")
        for nombre, cantidad in registro_ventas.items():
            print(f"- {nombre}: {cantidad} unidades")

        # Determina el producto con más unidades vendidas
        mas_vendido = max(registro_ventas, key=registro_ventas.get)
        print(f"\nProducto más vendido: {mas_vendido} ({registro_ventas[mas_vendido]} unidades)")
    print("------------------------------")

def main():
    inventario = cargar_inventario()
    total_recaudado = 0.0  
    registro_ventas = {}    
    carrito = []
    total_actual = 0.0

    # Bucle infinito para mantener el programa en ejecución
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Bucle para agregar múltiples productos al carrito
            while True:
                print("\nProductos disponibles:")
                for key, prod in inventario.items():
                    print(f"[{key}] {prod['nombre']} - ${prod['precio']:.2f}")
                print("[0] Terminar carga")
                
                seleccion = input("Ingrese el código: ")
                
                if seleccion == "0":    # Condición de salida del sub-menú
                    break
                
                if seleccion in inventario: # Valida que el código exista en el inventario
                    try:    # Manejo de errores para evitar que ingrese letras en lugar de números
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