"""
Nesse código vamos avaliar a herança simples.
Aqui teremos

Veiculo <- Carro
Veiculo <- Moto
Veiculo < - Caminhao

Veiculo: cor, placa, numero de rodas
    ligar motor(),
    str

Caminhao: esta carregado
    esta carregado()

"""


class Veiculo:
    def __init__(self, cor, placa, n_rodas):
        self.cor = cor
        self.placa = placa
        self.n_rodas = n_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: \t\n {', '.join([f'{chave} : {valor}' for chave, valor in self.__dict__.items()])}"
    
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass


moto1 = Motocicleta("Branca", "ABC-1243", 2)
carro1 = Carro("Cinza", "CAB - 1234", 4)

## Agora, vamos criar uma classe Caminhão que herda de Veiculo mas tem construtor que verifica se está carregado:
## Quando precisamos mudar a assinatura, é necessário inserir o super().metodo_classe_pai, que nesse caso é o __init__

class Caminhao(Veiculo):

    def __init__(self, cor, placa, n_rodas, carregado: bool):
        super().__init__(cor, placa, n_rodas)
        self.carregado = carregado

    
    def esta_carregado(self):
        print(f"{'Sim, ' if self.carregado else 'Não '} está carregado")


caminhao1 = Caminhao("Branco", "ACB-1234", 8, True)

print(moto1)
print(carro1)
print(caminhao1)

caminhao1.esta_carregado()