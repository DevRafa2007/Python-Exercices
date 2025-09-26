carros=["Fiat", "Chevrolet", "Ford", "Honda"]
carros.insert(1, "Jeep")
carros.pop(-1)
carros.append("Toyota")
print(carros)
print(len(carros))
ordem = carros.copy()
ordem.sort(key=len)
print(ordem)
