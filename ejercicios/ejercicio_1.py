def formateo(cadena):
    cadena = cadena[::-1]
    lista_cadena = cadena.split(",")
    return "{1} ha sacado un {0} de nota.".format(lista_cadena[0],lista_cadena[1])

def main():
    cadena = "zeréP nauJ,01"
    print(formateo(cadena))

if __name__ == "__main__":
    main()