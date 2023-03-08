import os
from helper import *
from re import search, IGNORECASE
from ejercicios.ejercicio_1 import main as main1
from ejercicios.ejercicio_2 import main as main2
from ejercicios.ejercicio_3 import main as main3
from ejercicios.ejercicio_4 import main as main4
from ejercicios.descomposicion import main as main5
from ejercicios.ejercicio_6 import main as main6
from ejercicios.ejercicio_7 import main as main7


print()
print("    El número mágico    ")
print()


def main():
    while True:
        limpiar_pantalla()

        print("        Menu         \n")
        print("¿Que ejercicio desea ejecutar?")
        print("_____________________________")
        print("[1] [2] [3] [4] [5] [6] [7]")
        print("Introduzca el numero del ejercicio que desea ejecutar, de lo contrario introduzca 0 para salir")
        print("_____________________________")

        pedido = leer_texto()
        limpiar_pantalla()

        if search(r"^\s*1\s*$", pedido):
            main1()
        elif search(r"^\s*2\s*$", pedido):
            main2()
        elif search(r"^\s*3\s*$", pedido):
            print(main3())
        elif search(r"^\s*4\s*$", pedido):
            main4()
        elif search(r"^\s*5\s*$", pedido):
            main5()
        elif search(r"^\s*6\s*$", pedido):
            main6()
        elif search(r"^\s*7\s*$", pedido):
            main7()
        elif search(r"^\s*0\s*$", pedido):
            print("saliendo...")
            break
        
        input("\nPresiona ENTER para continuar...")
        limpiar_pantalla()

if __name__ == "__main__":
    main()
