# Ingresar nombre de juegos
# Precio del juego
# Año de lanzamiento
# Fabricante
import menu
import new_inventory

juegos = []
attributes = {}

def storeGameInventory():
    print("\n========================TIENDA EL GAMER GEEK====================================")
    print("\nFavor de leer las instrucciones:")
    action = menu.instructions()
    while (int(action) != 4):
        if (int(action) == 1):
            name = new_inventory.game_name()
            juegos.append(name)
            details = new_inventory.add_entry_to_dict()
            attributes[name] = details
            print("\n \n=======================MENU================================")
            action = menu.in_menu()

        elif (int(action) == 2):
            print("\n\n========================INVENTARIO==========================")
            for x in juegos:
                print(f"{x} tiene un costo de ${attributes[x]['price']} y fue lanzado el año {attributes[x]['year']}")
            print("\n \n=======================MENU================================")
            action = menu.in_menu()

        elif (int(action) == 3):
            print("\n\n==========================MENU DE BORRAR============================")
            print("Para borrar el juego digite el nombre")
            for x in juegos:
                print(x)
            delete = input("Ingrese el nombre del juego que desea borrar, de lo contratio digite 'salir' para salir del menu de borrar: ")
            if ( delete != 'salir'):
                attributes.pop(delete)
                juegos.remove(delete)
            
            print("\n \n=======================MENU================================")
            action = menu.in_menu()
        else:
            print(f"'{str(action)}' no es una opción")
            action = menu.in_menu()
    print("Hasta pronto")
storeGameInventory()
