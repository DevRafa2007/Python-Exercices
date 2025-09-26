valores=[1, 2, 3, 4, 5, 6, 7, 8]
pares = list(filter(lambda x: x % 2 == 0, valores))
# ou pares = [x for x in valores if x % 2 == 0]
print(pares)