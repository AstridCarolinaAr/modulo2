def posicion_letras():
    '''

    :return:
    '''
    while True:
            Frase = str(input("escribe la frase corresponidente"))
            palabra = str(input("escribe la palabra que necesitas saber la posicion"))
            largo_palabra = len(palabra)
            posiciones_encontradas = []
            for indice, caracter in enumerate(Frase):
                fragmento = Frase[indice: indice + largo_palabra]
                if fragmento == palabra:
                 posiciones_encontradas.append(indice)
            if posiciones_encontradas:
                print(f" La palabra '{palabra}' se encontró en las siguientes posiciones:")
                print(posiciones_encontradas)
            else:
                print(f" La palabra '{palabra}' no se encuentra en la frase.")
            break



def main():
    posicion_letras()


if __name__ == '__main__':
    main()
