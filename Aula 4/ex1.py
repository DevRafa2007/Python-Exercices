import math

def bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None
    elif delta == 0:
        x = -b / (2*a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return (x1, x2)
    

print ("Digite os coeficientes a, b e c de uma equação do 2º grau:")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
raizes = bhaskara(a, b, c)
if raizes is None:
    print("A equação não possui raízes reais.")
elif len(raizes) == 1:
    print(f"A equação possui uma raiz real: {raizes[0]:.2f}")
else:
    print(f"A equação possui duas raízes reais: {raizes[0]:.2f} e {raizes[1]:.2f}")