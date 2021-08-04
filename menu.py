# Agregar
# Mostrar lista
# Detalles de un juego
import new_inventory

def instructions():
    print("Ingrese el número adecuado con respecto a cada acción.")
    print("\n1- Ingresar un nuevo juego\n2- Mostrar la lista de juegos\n3- Borrar un juego\n4- Salir del inventario")
    action = input("\nDigíte la acción: ")
    return action

def in_menu():
    print("\n1- Ingresar un nuevo juego\n2- Mostrar la lista de juegos\n3- Borrar un juego\n4- Salir del inventario")
    action = input("\nDigíte la acción: ")
    return action