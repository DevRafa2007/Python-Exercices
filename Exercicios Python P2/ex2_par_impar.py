"""Função `eh_par` retorna True se for par, False caso contrário.
"""

def eh_par(numero):
    return numero % 2 == 0


def main():
    print("Exercício 2 - Par ou Ímpar")
    n = int(input("Digite um número inteiro: "))
    if eh_par(n):
        print(f"{n} é par.")
    else:
        print(f"{n} é ímpar.")


if __name__ == '__main__':
    main()
