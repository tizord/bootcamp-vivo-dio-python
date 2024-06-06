"""
Aula de Introdução a POO - Vivo Python Backend

Desafio: João tem uma bicicletaria e quer registrar as vendas de suas bicicletas.
Crie um programa onde João informa:
    cor,
    modelo,
    ano e
    valor
da bicicleta vendida.

A Bicicleta pode:
 Buzinar,
 Parar e 
 Correr
"""

class Bicicleta:

    def __init__ (self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Bibiiiiiii")
    
    def parar(self):
        print("O freio foi apertado...")
        print("A bicicleta está parando...")
        print("A bicicleta está parada")
    
    def correr(self):
        print("A bicicleta está sendo pedala mais rápido...")
        print("A bicicleta está correndo")

    ## Agora repare no método __str__ que serve para exibir o objeto!

    # def __str__(self):
    #     return f"Bicicleta: \n\tCor: {self.cor}\n\tModelo: {self.modelo}\n\tAno: {self.ano}\n\tValor: {self.valor}"
    
    ## Mas podemos ir além e usar alguns atributos dados pelo Python para deixar mais automático:

    def __str__(self):
        return f"{self.__class__.__name__}: \n\t {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

"""
    Vamos avaliar o código acima:
    self.__class__.__name__ -> Traz o nome da classe do objeto. Chamar assim, permite mudar o nome da classe sem ter que mudar o código.
    Usamos list comprehension e nele trazemos:
    self.__dict__.items() -> Traz o par atributo e valor do atributo, de todos os atributos do objeto. O items() é para poder desempacotar.
    A vantagem de fazer da forma acima é, caso aumente os atributos da classe, não é necessário refatorar.
"""


b1 = Bicicleta("Preta", "Caloi", 2020, 500)
b2 = Bicicleta("Vermelha", "Top", 2024, 1000)

b1.buzinar()
b2.parar()

### Vejamos uma coisa interessante:
# b2.buzinar() == Bicicleta.buzinar(b2)

print(b1)