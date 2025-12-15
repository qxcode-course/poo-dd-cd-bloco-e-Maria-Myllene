from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__ (self, id: str, tipo: str):
        self.__id = id
        self.__tipo = tipo
        self.horaEntrada: int = 0 
    
    def __str__ (self):
        return (self.__tipo.rjust(10, "_") + " : " + self.__id.rjust(10, "_") + " : " + str(self.horaEntrada))
    
    @abstractmethod
    def calcularValor (self):
        pass

    def getId (self):
        return self.__id
    
    def getTipo (self):
        return self.__tipo


class Estacionamento:
    def __init__ (self):
        self.veiculos: list [Veiculo] = []
        self.horaAtual: int = 0
    
    def __str__ (self):
        saida = []
        for v in self.veiculos:
            saida.append(str(v))
        saida.append(f"Hora atual: {self.horaAtual}")
        return "\n".join(saida)
    
    def addTempo (self, tempo: int):
        self.horaAtual += tempo

    def estacionar (self, veiculo: Veiculo):
        veiculo.horaEntrada = self.horaAtual
        self.veiculos.append(veiculo)
    
    def procurarVeiculo (self, id: str):
        for pessoa in self.veiculos:
            if pessoa != None and pessoa.getId() == id:
                return pessoa
        return None
    
    def pagar (self, id: str):
        veiculo = self.procurarVeiculo(id)
        if veiculo == None:
            print("fail: veiculo nao encontrado")
            return
        valor = veiculo.calcularValor(self.horaAtual)
        print(f"{veiculo.getTipo()} chegou {veiculo.horaEntrada} saiu {self.horaAtual}. Pagar R$ {valor:.2f}")
    
    def sair (self, id: str):
        veiculo = self.procurarVeiculo(id)
        self.veiculos.remove(veiculo)


class Bike (Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Bike")
    
    def calcularValor(self, horaSaida: int):
       horaSaida += self.horaEntrada
       valor: float = 3.00
       return valor
    

class Moto (Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Moto")
    
    def calcularValor(self, horaSaida: int):
        valor = horaSaida - self.horaEntrada
        valorTotal = valor / 20
        return valorTotal

class Carro(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Carro")
    
    def calcularValor(self, horaSaida: int):
        valor = horaSaida - self.horaEntrada
        valorTotal = valor / 10
        if valorTotal < 5:
            valorTotal = 5
        return valorTotal


def main():
    veiculo = Estacionamento()
       
    while True:
        line = input()
        args: list[str] = line.split(" ")
        print("$" + line)

        if args [0] == "end":
            break
        elif args [0] == "show":
            print (veiculo)
        elif args [0] == "tempo":
            time = int(args[1])
            veiculo.addTempo(time)
        elif args [0] == "estacionar":
            tipo = args[1]
            id = args[2]
            meioTransporte = None
            if tipo == "bike":
                meioTransporte = Bike(id)
            elif tipo == "moto":
                meioTransporte = Moto(id)
            elif tipo == "carro":
                meioTransporte = Carro(id)
            else:
                print("fail: tipo invalido")

            veiculo.estacionar(meioTransporte)
        elif args[0] == "pagar":
            id = args[1]
            veiculo.pagar(id)
        else:
            print ("fail: comando invalido")

main()