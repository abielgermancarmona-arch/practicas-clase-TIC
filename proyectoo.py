#mi proyecto

Productos =[]
Salir = False
while Salir ==False:
    print("-----Menu De La Tienda-----")
    print("1. Registrar Producto")
    print("2. Buscar Producto")
    print("3. Comprar Producto")
    print("................")

    opcion=unput("Elige una Opcion")
    if opcion=="1":
        print("Registrar Produto")
        nombre=input("Nombre del Producto")
        codigo=input("Codigo del Producto")
        precio=float(input("precio del producto"))

        Producto={
            "nombre": nombre,
            "codigo": codigo,
            "precio": precio}
        Productos.append(Producto)
        print("Producto Registrado con Exito")
    elif opcion == "2":
        print("Buscar Producto")
        codigo_buscar=input("Ingresa el Codigo del Producto:")
        encontrado=False
        i=0

        while i<len(Productos)and encontrado==False:
            if producto[i]["codigo"]==codigo_buscar:
                print("Producto encontrado:")
                print("Nombre:", Productos[i]["nombre"])
                print("codigo:", Productos[i][codigo])
                print("Precio:", Productos[i]["precio"])
                encontrado=True
            i=i+1
        if encontrado==False:
            print("Producto no Encntrado")
    elif opcion =="3":
        print("comprar producto")
        codigo_comprar=input("Ingresa el codigo del producto a coprar:")
        encontrado=False
        i=0

        while i<len(Productos)and encontrado ==False:
            if Productos[i]["codigo"]==codigo_comprar:
                encontrado=True
                print("producto:",Productos[i]["nombre"])
                print("Precio:",Productos[i]["precio"])

                dinero=float(input("ingresa la cantidad de dinero:"))

                if dinero>=Productos[i]["precio"]:
                    cambio=dinero-Productos[i]["precio"]
                    print("Compra exitosa!")
                    print("Tu cambio es:", cambio)
                else:
                    print("no valido")
                i=i+1
            if encontrado == False:
                print("Producto no ncontrado")
            elif opcion =="4":
                print("Gracias por Usar Nuestra Tienda, Hasta Luego!!")

            else:
                print("opcion no valida, intentar de nuevo")
