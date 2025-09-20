print("Digite 3 números inteiros:")
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Terceiro número: "))

numeros = [num1, num2, num3]
numeros.sort()

print("Números em ordem crescente:", *numeros)