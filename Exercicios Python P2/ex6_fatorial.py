"""Exercício 6: calcula o fatorial de um número inteiro positivo.
Função `fatorial` lida com 0! = 1 e levanta ValueError para negativos.
"""

def fatorial(n):
    if n < 0:
        raise ValueError("Fatorial não definido para números negativos")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def main():
    print("Exercício 6 - Fatorial")
    n = int(input("Digite um número inteiro não-negativo: "))
    try:
        print(f"{n}! = {fatorial(n)}")
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
