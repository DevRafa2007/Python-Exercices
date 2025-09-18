
numeros = list(map(int, input("Digite números inteiros separados por espaço: ").split(",")))
numeros.sort()

div = list(filter(lambda x: x % 7 == 0, numeros))

print("Números divisíveis por 7:", div)