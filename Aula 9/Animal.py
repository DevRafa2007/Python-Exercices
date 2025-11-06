class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def apresentar(self):
        return f"Olá, meu nome é {self.name} e eu sou um {self.species}."