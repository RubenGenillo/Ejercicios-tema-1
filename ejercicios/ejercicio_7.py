def agregar_una_vez(lista, el):
    if el not in lista:
        lista.append(el)
    else:
        raise ValueError("Imposible añadir elementos duplicados => [{}]".format(el))
    return lista

def main():
    lista = []
    agregar_una_vez(lista, 10)
    agregar_una_vez(lista, -2)
    agregar_una_vez(lista, "Hola")
    print(lista)    

if __name__ == "__main__":
    main()