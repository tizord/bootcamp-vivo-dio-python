"""
Nesse código vamos avaliar a herança múltipla onde

Animal <- Mamífero
Animal <- Ave

Mamífero <- Cachorro
Mamífero <- Gato
Mamífero <- Leão

Mamífero, Ave <- Ornitorrinco


"""

class Animal:
    def __init__(self, n_patas):
        self.n_patas = n_patas

    def __str__(self):
        return f"{self.__class__.__name__}: \t\n {', '.join([f'{chave} : {valor}' for chave, valor in self.__dict__.items()])}"
    
"""
Agora, vamos avaliar formas de trazer o assinatura da classe pai:
# Uma forma: usando **kwargs
# lembrando que dessa forma, os argumentos vem como pares chave, valor, o que implica em passar os argumentos de forma nomeada
# E isso deixa o código mais complexo para dar manutenção

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)

        
Abaixo, vamos ver uma forma mais fácil:
"""

class Mamifero(Animal):
    def __init__(self, n_patas, cor_pelo, *args, **kwargs):
        super().__init__(n_patas, *args, **kwargs)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, n_patas, cor_bico, *args, **kwargs):
        super().__init__(n_patas, *args, **kwargs)
        self.cor_bico = cor_bico


class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, n_patas, cor_pelo, cor_bico):
        super().__init__(n_patas, cor_pelo, cor_bico)

    


"""
Para o primeiro caso, usando **kwargs, teríamos que instanciar o objeto assim:

gato1 = Gato(n_patas=4, cor_pelo="Preto")
orni1 = Ornitorrinco(n_patas=4, cor_pelo="Marrom", cor_bico="Laranja")
print(orni1)

Para o segundo método, podemos instanciar assim:
"""
animal = Animal(2)
gato1 = Gato(4, "Preto")
orni1 = Ornitorrinco(4, "Marrom", "Laranja")
print(f"{gato1}\n{orni1}")
