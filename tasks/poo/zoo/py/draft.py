from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__ (self, nome: str):
        self.__nome = nome
    
    def apresentar_nome(self):
        return (f"Eu sou um {self.__nome}")
    
    @abstractmethod
    def fazer_som(self):
        pass

    @abstractmethod
    def mover(self):
        pass

class Leao (Animal):
    def __init__ (self, nome: str):
        super().__init__("Leão")
    
    def fazer_som(self):
        return "RRRUUUAAAARRRRR"
    
    def mover(self):
        return "Correr"

class Cobra (Animal):
    def __init__ (self, nome: str):
        super().__init__("Cobra")
    
    def fazer_som(self):
        return "SSSSSS"
    
    def mover(self):
        return "Rastejar"

class Galinha (Animal):
    def __init__ (self, nome: str):
        super().__init__("Galinha")
    
    def fazer_som(self):
        return "PÓ PÓ PÓ PÓ"
    
    def mover(self):
        return "Ciscar"   

def main():
    animais = [Leao("Leão"), Cobra("Cobra"), Galinha("Galinha")]
    print (animais)
    while True:
        line = input()
        args: list[str] = line.split(" ")
        if args [0] == "end":
            break
        elif args [0] == "show":
            for animal in animais:
                print (animal)
        else:
            print("fail: comando invalido")

main()
