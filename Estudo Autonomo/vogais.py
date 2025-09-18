def filtrar(lista):
    resultado = [x for x in lista if x.strip() and x.strip()[0].lower() in "aeiou"]
    return resultado

lista = input("Digite palavras separadas por espaço: ").split()
print("As palavras que começam com vogais são: ", *filtrar(lista))