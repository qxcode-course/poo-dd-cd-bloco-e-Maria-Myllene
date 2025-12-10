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

    @abstractmethod
    def cor(self):
        pass

    @abstractmethod
    def quantidade_patas(self):
        pass

class Leao (Animal):
    def __init__ (self, nome: str):
        super().__init__(nome)
    
    def fazer_som(self):
        return "RRRUUUAAAARRRRR"
    
    def mover(self):
        return "Correr"
    
    def cor(self):
        return "Amarelo e marrom"
    
    def quantidade_patas(self):
        return 4

class Cobra (Animal):
    def __init__ (self, nome: str):
        super().__init__(nome)
    
    def fazer_som(self):
        return "SSSSSS"
    
    def mover(self):
        return "Rastejar"
    
    def cor(self):
        return "Verde"
    
    def quantidade_patas(self):
        return 0

class Galinha (Animal):
    def __init__ (self, nome: str):
        super().__init__(nome)
    
    def fazer_som(self):
        return "PÓ PÓ PÓ PÓ"
    
    def mover(self):
        return "Ciscar"

    def cor(self):
        return "Branca" 
    
    def quantidade_patas(self):
        return 2

def apresentar(animal: Animal):
    print (f"Eu sou um(a) {animal.apresentar_nome()} - som: {animal.fazer_som()}, movimento: {animal.mover()}, cor: {animal.cor()}, quantidade de patas: {animal.quantidade_patas()}")
    print(type(animal))

leao = Leao("Leão")
cobra = Cobra("Cobra")
galinha = Galinha("Galinha")

apresentar(leao)
apresentar(cobra)
apresentar(galinha)



