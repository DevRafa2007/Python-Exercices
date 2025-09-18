def filtrar(lista):
    resultado = [nome for nome in lista if nome.strip() and nome.strip()[0].upper() == "A"]
    return resultado


lista = list(map(str, input("Digite palavras separadas por espaço: ").split()))

resultado = filtrar(lista)

print("Essas são as palavras que iniciam com 'A': ", resultado)

