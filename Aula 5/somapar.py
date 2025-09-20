def par(s):
    return s % 2 == 0

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
s = n1 + n2

if par(s):
    print(f"A soma de {n1} + {n2} é {s} e isso é par")
else:
    print(f"A soma de {n1} + {n2} é {s} e isso é impar")