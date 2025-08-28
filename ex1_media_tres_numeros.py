
def media_tres(a, b, c):
    return (a + b + c) / 3.0


def main():
    print("Exercício 1 - Média de três números")
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    c = float(input("Digite o terceiro número: "))
    resultado = media_tres(a, b, c)
    print(f"A média dos três números é: {resultado}")


if __name__ == '__main__':
    main()
