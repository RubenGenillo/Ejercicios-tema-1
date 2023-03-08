def separacion(listapares, listaimpares, lista, tamaño):
    if lista[tamaño] % 2 == 0:
        listapares.append(lista[tamaño])
    else:
        listaimpares.append(lista[tamaño])
    if tamaño == 0:
        return listapares, listaimpares
    else:
        separacion(listapares, listaimpares, lista, tamaño-1)

def separar(lista):
    tamaño = len(lista)
    listapares = []
    listaimpares = []
    separacion(listapares, listaimpares, lista, tamaño-1)
    listapares.sort()
    listaimpares.sort()
    return listapares, listaimpares



def main():
    pares, impares = separar([6,5,2,1,7])
    print(pares)
    print(impares)

if __name__ == "__main__":
    main()















