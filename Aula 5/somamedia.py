soma = 0 
print("Calcule a média de 6 numeros: ")
for i in range(6):
    n = int(input(f"Digite o {i+1}º número:"))
    soma +=n

m = soma / 6
print(f"A média da soma dos números é {m}")