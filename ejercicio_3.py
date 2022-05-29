 # Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $3.500 y si es mayor de 18 años, $8.000.
def precios(edad):
    contador_a = 0
    contador_b = 0
    contador_c = 0
    if edad < 4:
        precio = 0
        contador_a =+1
    elif edad <= 18:
        precio = 3500
        contador_b =+1
    else:
        precio = 8000
        contador_c =+1
    return precio, contador_a, contador_b, contador_c

def boleta(clientes):
    precio = 0
    contador_a = 0
    contador_b = 0
    contador_c = 0
    for contador in range(clientes):
        edad = int(input("Ingrese la edad del cliente: "))
        total = precios(edad)
        precio = precio + int(total[0])
        contador_a = contador_a + int(total[1])
        contador_b = contador_b + int(total[2])
        contador_c = contador_c + int(total[3])

    if contador_a > 0:
        print("Menor a 4 años $0 x"+str(contador_a)+(" = $")+str(0*contador_a))
    if contador_b > 0:
        print("Entre 4  y 18 años $3500 x"+str(contador_b)+(" = $")+str(3500*contador_b))
    if contador_c > 0:
        print("Mayor a 18 años $8000 x"+str(contador_c)+(" = $")+str(8000*contador_c))
        
    print("Total: $"+str(precio))

def main():
    clientes = int(input("Ingrese la cantidad de clientes: "))
    if clientes > 0:
        boleta(clientes)
    else:
        print("Ingrese un valor válido.")

if __name__ == '__main__':
    main()