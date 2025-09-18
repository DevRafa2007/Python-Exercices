import random
import string

n = int(input("Digite um numéro de carcteres para sua senha: "))
caracteres = string.ascii_letters + string.digits
lista = [random.choice(caracteres) for _ in range(n)]

senha = "".join(lista)

print(f"Sua senha é {senha}")