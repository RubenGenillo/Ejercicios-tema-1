def inputint(texto):
  while True:
    num = input(texto)
    try:
        num = int(num)
    except:
        if num == "":
            print("Debe de darse un número entero")
        else:
         pass 
    else:    
     if num > 0:
         return num

def convertidor(num):
    numstr = str(num)
    listnumeros = []
    for elementos in range(len(numstr)):
        listnumeros.append("0"*elementos + numstr[elementos] + "0"*(len(numstr)-elementos-1))
    return listnumeros[::-1]

def main():
    numero = inputint("Dame un número entero positivo\n> ")
    return convertidor(numero)

if __name__ == "__main__":
    numeros = main()
    for numero in numeros:
        print(numero)