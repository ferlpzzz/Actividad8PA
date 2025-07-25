products = []
while True:
    print("1. Agregar un producto a la lista")
    print("2. Modificar un producto existente")
    print("3. Eliminar un producto")
    print("4. Ver todos los productos")
    print("5. Salir del programa")
    option = input("Ingrese una opcion: ")
    match option:
        case "1":
            product = input("Ingrese el producto: ")
            products.append(product)
            print("Se ha agregado el producto")
        case "2":
            print(f"Los productos actuales son: {products}")
            name_modif = int(input("Ingrese el indice del producto que desea modificar: "))
            new_element =   input("Ingrese el nombre del producto nuevo: ")
            products[name_modif] = new_element
            print("Producto modificado")
        case "3":
            print (f"Los productos actuales son: {products}")
            product_to_remove = input("Ingrese el producto a eliminar: ")
            products.remove(product_to_remove)
            print("Producto eliminado.")
        case "4":
            print(f"Los productos actuales son: {products}")
        case "5":
            print("Gracias por usar nuestro programa.")
            break
        case _:
            print("Error. Ingresa una opción válida.")
            print("BOBO")

