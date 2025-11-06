from Animal import Animal
class Cachorro(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Cachorro")
        self.breed = breed

    def emitirSom(self):
        return "Latir"
    def correr(self):
        return f"{self.name} está correndo!"