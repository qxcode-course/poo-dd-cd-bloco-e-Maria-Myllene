from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__ (self, nome: str):
        self.__nome = nome
    
    def apresentar_nome(self):
        return self.__nome

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

def apresentar(animal: Animal):
    print (f"Eu sou um(a) {animal.apresentar_nome()} - som: {animal.fazer_som()}, movimento: {animal.mover()}")
    print(type(animal))

leao = Leao("Leão")
cobra = Cobra("Cobra")
galinha = Galinha("Galinha")

apresentar(leao)
apresentar(cobra)
apresentar(galinha)

lion = Leao("Lion")
cobrita = Cobra("Snake")
chicken = Galinha ("Pó pó")

apresentar(lion)
apresentar(cobrita)
apresentar(chicken)


