palavras = input("Digite uma frase: ").split()

ranking = {p: len(p) for p in palavras}
ordenado = sorted(ranking.items(), key=lambda x: x[1], reverse= True)

for palavra, tamanho in ordenado:
    print(f"{palavra} -> {tamanho}")