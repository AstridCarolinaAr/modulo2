def definir_impar_par():
     '''
     define si el numero ingresado es par o impar y adicionalmente si es multiplo de 5
     '''
     while True:
        try:
                numero = int(input("escriba el numero que desea comprobar"))
                if numero<0:
                    print("no coloques numeros negativos")
                    numero = int(input("escriba el numero que desea comprobar"))
                    continue
                else:
                    if numero %2==0:
                        print(f"el numero {numero} es par")

                    else:
                        print(f"el numero {numero} es impar")

                    if numero % 5 == 0:
                        print(f"y el numero {numero} es multiplo de 5")
                    break
        except ValueError:
            print("los caracteres ingresados son incorectos \nten en cuenta que deben ingresar ser numeros enteros")
            numero = int(input("escriba el numero que desea comprobar"))

def main():
    definir_impar_par()

if __name__ =='__main__':
    main()