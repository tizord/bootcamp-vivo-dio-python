'''
Bootcamp - Vivo - Python AI Backend Developer

Desafio 3 - Fazer o sistema bancário em POO

'''

from abc import ABC, ABCMeta, abstractmethod, classmethod
import datetime

class Cliente:
    def __init__(self, endereco: str):
        self._endereco = endereco
        self._contas = []

        # Por que ele não recebe contas? Contas não é um atributo no UML?
        # Por que ele não colocou esses atributos como privado sendo que no UML está com o '-' na frente?
        # Se passarmos o tipo dos parâmetros, indica erro nos tipos Conta e Transação por serem definidos só depois.. como resolver?
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome: str, data_nascimento, cpf: str, endereco: str):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf

class Conta:
    def __init__(self, numero: int, cliente: Cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

        #Como saber qual atributo vem por parâmetro e qual não vem?

    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: int):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor: float):
        saldo = self.saldo
        execeu_saldo = valor > saldo

        if execeu_saldo:
            print("\tVocê não possui saldo suficiente")
        elif valor > 0:
            self.valor -= valor
            print('\tSaque realizado com sucesso.')
            return True
        else:
            print('\tOperação falhou. O valor informado é inválido')
        
        return False

    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
            print("\tDepósito realizado com sucesso.")
            return True
        else:
            print('\tOperação falhou. O valor informado é inválido')
        
        return False

class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente: Cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite,
        self._limite_saques = limite_saques

    @property
    def limite(self):
        return self._limite
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.trasacoes if transacao["tipo"]== Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print('\tOperação falhou. Valor do saque excede o limite.')
        elif excedeu_saques:
            print('\tOperação falhou. Número máximo de saques excedido.')
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
        Agência:\t{self.agencia}
        C\C:\t\t{self.numero}
        Titular:\t{self.cliente.nome}
        """

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def registrar(self, conta: Conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
        

class Saque(Transacao):
    def __init__(self, valor:float):
        self._valor = valor
    #Por que não usamos super?    
    
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes


    def adicionar_transacao(self, transacao: Transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )






