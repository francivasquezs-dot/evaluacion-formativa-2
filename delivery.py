
while True:
        precios = {
            "Pikachu Roll": 4500,
            "Otaku Roll": 5000,
            "Pulpo Venenoso Roll": 5200,
            "Anguila Eléctrica Roll": 4800
        }
        carrito = {
            "Pikachu Roll": 0,
            "Otaku Roll": 0,
            "Pulpo Venenoso Roll": 0,
            "Anguila Eléctrica Roll": 0
        }
        while True:
            print("\n--- MENÚ DELIVERY SUSHI ---")
            print("1. Pikachu Roll $4.500 ")
            print("2. Otaku Roll $5.000 ")
            print("3. Pulpo Venenoso Roll $5.200 ")
            print("4. Anguila Eléctrica Roll $4.800 ")
            print("5. Terminar pedido")
            
            opcion = input("seleccione una opción, por favor. (1-5): ").strip()
            
            if opcion == "1":
                carrito["Pikachu Roll"] += 1
                print("¡Pikachu Roll agregado!")
            elif opcion == "2":
                carrito["Otaku Roll"] += 1
                print("¡Otaku Roll agregado!")
            elif opcion == "3":
                carrito["Pulpo Venenoso Roll"] += 1
                print("¡Pulpo Venenoso Roll agregado!")
            elif opcion == "4":
                carrito["Anguila Eléctrica Roll"] += 1
                print("¡Anguila Eléctrica Roll agregado!")
            elif opcion == "5":
                total_items = sum(carrito.values())
                if total_items > 0:
                    break
                else:
                    print("su pedido esta vacio. agregue un roll antes de terminar.")
            else:
                print("opcion no valida. intente nuevamente.")
        descuento_aplicado = 0
        
        while True:
            tiene_codigo = input("\n¿posee un codigo de descuento? (S/N): ").strip().upper()
            if tiene_codigo == "N":
                break
            elif tiene_codigo == "S":
                codigo = input("ingrese el codigo de descuento: ").strip()
                
                if codigo == "soyotaku":
                    descuento_aplicado = 0.10
                    print("¡codigo valido! Se aplicara un 10% de descuento.")
                    break
                else:
                    print("codigo no valido.")
                    opcion_error = input("presione ENTER para reingresar el codigo o 'X' para continuar sin descuento: ").strip().upper()
                    if opcion_error == "X":
                        break
            else:
                print("opcion no valida. ingrese S o N.")
        total_productos = sum(carrito.values())
        subtotal = sum(carrito[roll] * precios[roll] for roll in carrito)
        monto_descuento = int(subtotal * descuento_aplicado)
        total_final = subtotal - monto_descuento
        print("\n" + "*" * 30)
        print(f"TOTAL PRODUCTOS: {total_productos}")
        print("*" * 30)
        for roll, cantidad in carrito.items():
            print(f"{roll} : {cantidad}")
        print("*" * 30)
        print(f"Subtotal por pagar: ${subtotal}")
        print(f"Descuento por codigo: ${monto_descuento}")
        print(f"TOTAL: ${total_final}")
        print("*" * 30)
        otro_pedido = input("\n¿desea realizar otro pedido? (S/N): ").strip().upper()
        if otro_pedido != "S":
            print("¡gracias por comprar en nuestro delivery de sushi! hasta pronto.")
            break
