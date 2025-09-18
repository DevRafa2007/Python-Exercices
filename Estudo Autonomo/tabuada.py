n = int(input("Digite um número e veja a tabuada dele: "))

for i in range(1, 11):
    resultado = n*i
    print(f"{n} x {i} = {resultado}")