n = int(input("Digite um número para ver os quadrados de 1 até seu número: "))

lista = range(1, n+1)
quadrados = list(map(lambda x: x**2, lista))

resultado = list(filter(lambda x: x%3== 0 or x%5==0, quadrados))

for i in lista:
    print("O quadrado de", i, "é", quadrados[i-1])
print("Os quadrados divisiveis por 3 ou 5 são: ", resultado)