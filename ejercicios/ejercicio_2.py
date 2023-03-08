def inputint(texto, min, max):
  while True:
    num = input(texto)
    try:
        num = int(num)
    except:
        pass 
    else:    
     if num <= max and num >= min:
         return num

def main():
    numero_magico = 12345679
    numero_usuario = inputint("Dame un número entre 1 y 9\n> ", 1, 9)
    numero_usuario *= 9
    numero_magico *= numero_usuario
    print(numero_magico)

if __name__ == "__main__":
    main()