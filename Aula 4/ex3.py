import math 

def areaCirculo(raio):
    return math.pi * raio**2

print("Digite o raio do círculo:")
raio = float(input("Raio: "))
area = areaCirculo(raio)
print(f"A área do círculo é: {area:.2f}")