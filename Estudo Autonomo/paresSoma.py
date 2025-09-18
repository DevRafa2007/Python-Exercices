def ehpar(lista):
    resultado = [n for n in lista if n % 2 == 0]
    return resultado
print("Veja os pares da lista e a soma deles")
lista = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))
resultado = ehpar(lista)
soma = sum(resultado)
print(f"Os números pares da lista são: {resultado}")
print(f"A soma dos números pares é: {soma}")