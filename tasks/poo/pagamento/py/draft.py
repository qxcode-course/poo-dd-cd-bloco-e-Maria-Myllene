from abc import ABC, abstractmethod
import datetime
import time
import sys


class Pagamento(ABC):
    def __init__ (self, valor: float, descricao: str):
        self.valor = valor
        self.descricao = descricao

    def resumo(self) -> str:
        return f"Pagamento de R$ {self.valor:.2f}: {self.descricao}"
    
    def validar_valor(self) -> None:
        if self.valor <= 0:
            raise ValueError("--- fail: valor invalido ---")

    @abstractmethod    
    def processar(self):
        pass


class CartaoCredito(Pagamento):
    def __init__(self, numero: int, nome_titular: str, limite_disponivel: float, valor: float, descricao: str):
        super().__init__(valor, descricao)
        self.numero = numero
        self.nome_titular = nome_titular
        self.limite_disponivel = limite_disponivel

    def processar(self):
        self.validar_valor()
        if self.valor > self.limite_disponivel:
            print ("--- fail: limite indisponivel ---")
            return
        self.limite_disponivel -= self.valor
        print ("| success: pagamento confirmado |")
        
    def resumo (self):
        return "\nCARTÃO DE CRÉDITO -\n" + super().resumo()

    def get_limite(self):
        print (f"(Dados do cartão)\nNome do Titular: {self.nome_titular} | Número do cartão: {self.numero}")
        return f"[limite disponivel: R$ {self.limite_disponivel:.2f}]"
    

class Pix(Pagamento):
    def __init__(self, chave: str, banco: str, valor: float, descricao: str):
        super().__init__(valor, descricao)
        self.chave = chave
        self.banco = banco
    
    def processar(self):
        self.validar_valor()
        print ("| success: pagamento confirmado |")
        print (f"PIX enviado via {self.banco} usando chave {self.chave}")
        return

    def resumo(self):
        return "\nPIX -\n" + super().resumo()
    

class Boleto(Pagamento):
    def __init__(self, codigo_barras: int, vencimento: datetime.date, valor: float, descricao: str):
        super().__init__(valor, descricao)
        self.codigo_barras = codigo_barras
        self.vencimento = vencimento

    def processar(self):
        self.validar_valor()
        if self.vencimento < datetime.date.today():
            print(f"Código de barras: {self.codigo_barras} | Vencimento: {self.vencimento}")
            raise ValueError("--- fail: boleto vencido ---")
        
        print(f"Boleto gerado. Aguardando pagamento...")
        print(f"Código de barras: {self.codigo_barras} | Vencimento: {self.vencimento}")

        for i in range(3, 0, -1):
            print("Aguardando pagamento." + "." * (i - 1), end="\r")
            sys.stdout.flush()
            time.sleep(1)

        print(" " * 40, end='\r')
        print("| success: pagamento confirmado! |")

    def resumo(self):
        return "\nBOLETO -\n" + super().resumo()    

def processar_pagamento(pagamento: list [Pagamento]):
    for pag in pagamento:
        try: 
            print(pag.resumo())
            pag.processar()
            if isinstance(pag, CartaoCredito):
                print(pag.get_limite())
        except ValueError as e:
            print(e)

pagamento: Pagamento = [
    Pix(valor = 150, descricao = "Camisa esportiva", chave = "email@ex.com", banco = "Banco XPTO"),
    CartaoCredito(valor = 400, descricao = "Tênis esportivo", numero = "1234 5678 9123 4567", nome_titular = "Cliente X", limite_disponivel = 500),
    Boleto(valor = 89.90, descricao = "Livro de Python", codigo_barras = "123456789000", vencimento = datetime.date(2025, 1, 10)),
    CartaoCredito(valor = 800, descricao = "Notebook",  numero = "9999 8888 7777 6666", nome_titular = "Cliente Y", limite_disponivel = 700),
    Pix(valor = 0.00, descricao = "Manga do vizinho", chave = "email@ex.com", banco = "Banco XPTO"),
    Boleto(valor = 50.46, descricao = "Camiseta de One Piece", codigo_barras = "123456789000", vencimento = datetime.date(2025, 12, 30)),
]

processar_pagamento(pagamento)