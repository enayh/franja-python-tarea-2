# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
def main():
    frase = input("Ingrese una frase: ")
    letra = input("Ingrese una letra: ")

    cantidad = 0

    for contador in range(len(frase)):
        letra_aux = frase[contador]
        if letra_aux == letra.lower() or letra_aux == letra.upper():
            cantidad += 1
    
    print("La letra "+letra+" aparece "+str(cantidad)+" veces en la frase.")

if __name__ == '__main__':
    main()