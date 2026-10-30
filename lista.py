# Ordena y no permite datos repetidos
# Definicion de las estructuras de datos

class Contacto:
    def __init__(self, num: str, nombre: str, red: str, rank: int):
        self.num = num
        self.nombre = nombre  # Order key
        self.red = red
        self.rank = rank
        self.next = None

    def print(self):
        print(f"{self.nombre} | {self.num} : {self.red} - {self.rank}")


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new: Contacto) -> bool:
        '''Devuelve True si inserta y False si el nombre ya existe'''

        # Cuando la lista esta vacia
        if self.head == None:
            self.head = new
            return True

        # Evitar nombres repetidos en la cabecera
        if new.nombre.lower() == self.head.nombre.lower():
            return False

        # Cuando el nuevo nodo debe ser la cabecera
        if new.nombre.lower() < self.head.nombre.lower():
            new.next = self.head
            self.head = new
            return True

        # Recorrer la lista para encontrar la posicion correcta
        previous = self.head
        temp = self.head.next

        while temp != None:

            # Evitar nombres repetidos
            if new.nombre.lower() == temp.nombre.lower():
                return False

            # Insertar antes del nodo actual
            if new.nombre.lower() < temp.nombre.lower():
                previous.next = new
                new.next = temp
                return True

            previous = temp
            temp = temp.next

        # Si llegamos al final, comprobar el ultimo nodo
        if new.nombre.lower() == previous.nombre.lower():
            return False

        # Insertar al final
        previous.next = new
        return True

    def print(self):
        if self.head == None:
            print("Lista vacia")
            return

        temp = self.head

        while temp != None:
            temp.print()
            temp = temp.next

    def remove(self, nombre: str) -> Contacto:
        '''Elimina un contacto por nombre y lo devuelve.
        Si no existe, devuelve None.
        '''

        # Cuando la lista esta vacia
        if self.head == None:
            return None

        # Cuando el contacto esta en la cabecera
        if nombre.lower() == self.head.nombre.lower():
            contacto = self.head
            self.head = self.head.next
            contacto.next = None
            return contacto

        # Buscar el contacto en el resto de la lista
        previous = self.head
        temp = self.head.next

        while temp != None:

            if nombre.lower() == temp.nombre.lower():
                previous.next = temp.next
                temp.next = None
                return temp

            # Como la lista esta ordenada, podemos detenernos
            # si el nombre buscado deberia ir antes de temp
            if nombre.lower() < temp.nombre.lower():
                return None

            previous = temp
            temp = temp.next

        # El contacto no existe
        return None
