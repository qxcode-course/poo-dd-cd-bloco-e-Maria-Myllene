from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__ (self, nome: str):
        self.__nome = nome
    
    def __str__(self):
        return f"Eu sou um(a) {self.__nome} - som: {self.fazer_som()}, movimento: {self.mover()}"
    
    @abstractmethod
    def fazer_som(self):
        pass

    @abstractmethod
    def mover(self):
        pass


class Leao (Animal):
    def __init__ (self, nome: str):
        super().__init__(nome)
    
    def fazer_som(self):
        return "RRRUUUAAAARRRRR"
    
    def mover(self):
        return "Correr"

class Cobra (Animal):
    def __init__ (self, nome: str):
        super().__init__(nome)
    
    def fazer_som(self):
        return "SSSSSS"
    
    def mover(self):
        return "Rastejar"

class Galinha (Animal):
    def __init__ (self, nome: str):
        super().__init__(nome)
    
    def fazer_som(self):
        return "PÓ PÓ PÓ PÓ"
    
    def mover(self):
        return "Ciscar"   

animais: list[Animal] = [Leao("Leão"), Cobra("Cobra"), Galinha("Galinha")]
for animal in animais:
    print (animal)
