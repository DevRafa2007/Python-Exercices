def divisivel(num):
    return num % 5 == 0

print("Descubra se um número é divisível por 5.")

n = int(input("Digite um número inteiro: "))
if divisivel(n):
    print(f"O número {n} é divisível por 5.")
else:
    print(f"O número {n} não é divisível por 5.")