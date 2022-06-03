# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
from cmath import pi

def area(radio):
    return round(pi * radio**2, 2)

def volumen(radio, altura):
    return round(area(radio)*altura, 2)

def main():
    print("1.- Área de un círculo.")
    print("2.- Volumen de un cilindro.")
    opcion = int(input("Qué desea calcular? "))

    if opcion == 1:
        radio = float(input("Ingrese un valor para el radio del círculo: "))
        ar = area(radio)
        print("El área del círculo es de "+str(ar))
    elif opcion == 2:
        radio = float(input("Ingrese un valor para el radio del cilindro: "))
        altura = float(input("ingrese un valor para la altura del cilindro: "))
        vol = volumen(radio, altura)
        print("El volumen del cilindro es: "+str(vol))
    else:
        print("Ingrese un valo válido.")

if __name__ == '__main__':
    main()