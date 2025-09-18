n = int(input("Digite um número para ver os quadrados de 1 até seu número: "))

dict = {}

for i in range(1, n+1):
    dict[i] = i**2
    print("O quadrado de", i, "é",dict[i])
