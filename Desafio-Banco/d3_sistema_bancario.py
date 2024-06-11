'''
Bootcamp - Vivo - Python AI Backend Developer

Desafio 3 - Fazer o sistema bancário em POO

'''

from abc import ABC, ABCMeta, abstractmethod

class Cliente:
    def __init__(self, endereco: str, contas: int):
        self._endereco = endereco
        self._contas = contas

    def realizar_transacao(conta: Conta, transacao: Transacao):
        pass

    def adicionar_conta(self, conta: Conta):
        pass

class PessoaFisica(Cliente):
    def __init__(self, endereco: str, contas: int, cpf: str, nome: str, data_nascimento: date):
        super().__init__(endereco, contas)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

class Conta:
    def __init__(self, saldo:float, numero: int, agencia:str, cliente: Cliente, historico: Historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    def saldo(self):
        pass

    def nova_conta(self, cliente: Cliente, numero: int):
        return Conta
    
    def sacar (self, valor: float):
        pass

    def depositar(self, valor: float):
        pass

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta: Conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor: float) -> None:
        super().__init__()
    
    def registrar(self, conta: Conta):
        pass

class Saque(Transacao):
    def __init__(self, valor:float):
        super().__init__()
        
    def registrar(self, conta: Conta):
        pass

class Historico:
    def adicionar_transacao(self, transacao: Transacao):
        pass

class ContaCorrente(Conta):
    def __init__(self, saldo: float, numero: int, agencia: str, cliente: Cliente, historico: Historico, limite: float, limite_saques: int):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite,
        self._limite_saques = limite_saques




