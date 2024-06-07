"""
Vamos avaliar dois cenários:
1) a classe Pessoa que contém um método para criar um objeto a partir da data de nascimento.
Ela recebe um objeto pessoa e terá que instânciar outro objeto pessoa, o que não é ideal.

Repare que no construtor de pessoa, temos que passar nome e idade = None, caso contrário o método não iria funcionar uma vez que o construtor pede 2 argumentos.

"""
class Pessoa:
    def __init__(self, nome=None, idade=None) -> None:
        self.nome = nome
        self.idade = idade

    def criar_de_data_nascimento(self, ano, mes, dia, nome):
        idade = 2024 - ano
        return Pessoa(nome, idade)
    
p = Pessoa("Thiago", 31)
print(p.nome, p.idade)

p = Pessoa().criar_de_data_nascimento(1993, 9, 11, "Thiago")
print(p.nome, p.idade)

"""
Dessa forma, é ideal transformar o método "criar_de_data_nascimento" em um método de classe. isso é feito usando o decorador @classmethod
Por convenção, quando usamos o @classmethod, não usamos a palavra "self" e sim "cls".

Por fim, como o método virou um método de classe, invocamos ele de forma diferente:

p = Classe.método_de_classe()

Por fim, criamos um método estático usando o decorador @staticmethod

"""
class Pessoa:
    def __init__(self, nome=None, idade=None) -> None:
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa("Thiago", 31)
print(p.nome, p.idade)

p = Pessoa.criar_de_data_nascimento(1993, 9, 11, "Thiago")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(17))
print(Pessoa.e_maior_idade(27))



########## Clase abstrata ###########

from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando")
    def desligar(self):
        print("Desligando")
    
    @property
    def marca(self):
        return "LG"

controle1 = ControleTV()
controle1.ligar()
controle1.desligar()