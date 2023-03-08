#pop (y insert )

#o append y que elimine el primero

class cola:
    def __init__(self, *args):
        self.lista = [*args]
    def __str__(self):
        return str(self.lista)
    def añadir(self, elemento):
        self.lista.append(elemento)
    def eliminar(self):
        self.lista.pop(0)


def main():
    print("Ejemplo de la estrcutura tipo cola creada: ")
    tareas = cola("investigar","comparar","resumir")
    print(tareas)
    tareas.añadir("codigo")
    print(tareas)
    tareas.eliminar()
    print(tareas)

if __name__ == "__main__":
    main()