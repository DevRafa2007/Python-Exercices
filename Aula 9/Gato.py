from Animal import Animal
class Gato(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Gato")
        self.color = color

    def miar(self):
        return "Miau Miau!"
    def cagar(self):
        return f"{self.name} está cagando!"