# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
def buscador(frase, letra):
    cantidad = 0
    for contador in range(len(frase)):
        letra_aux = frase[contador]
        if letra_aux == letra.lower() or letra_aux == letra.upper():
            cantidad += 1
    return cantidad

def main():
    frase = input("Ingrese una frase: ")
    letra = input("Ingrese una letra: ")
    
    cantidad = buscador(frase, letra)
    
    if cantidad > 0:
        print("La letra '"+letra+"' aparece "+str(cantidad)+" veces en la frase.")
    else:
        print("La letra '"+letra+"' no aparece en la frase.")

if __name__ == '__main__':
    main()