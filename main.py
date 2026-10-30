from lista import Contacto, LinkedList


def main():
    lista = LinkedList()

    c = Contacto("85458745", "Julissa Parrales", "Claro", 3)
    print("Insertado:", lista.insert(c))

    c = Contacto("69784521", "Julio Aragón", "Tigo", 4)
    print("Insertado:", lista.insert(c))

    c = Contacto("85458745", "Julissa Parrales", "Claro", 3)
    print("Insertado:", lista.insert(c))

    c = Contacto("78548569", "Paulo Andino", "Claro", 5)
    print("Insertado:", lista.insert(c))

    print("\n--- Lista de contactos ---")
    lista.print()

    print("\n" + "*" * 30)

    eliminado = lista.remove("Julissa Parrales")

    if eliminado != None:
        print("Contacto eliminado:")
        eliminado.print()
    else:
        print("El contacto no existe.")

    print("\n--- Lista despues de eliminar ---")
    lista.print()


main()
