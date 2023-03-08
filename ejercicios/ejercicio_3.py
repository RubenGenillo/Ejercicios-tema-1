def main():
    lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
    lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
    lista_3 = list(set(lista_1).intersection(set(lista_2)))
    return lista_3


if __name__ == "__main__":
    print(main())