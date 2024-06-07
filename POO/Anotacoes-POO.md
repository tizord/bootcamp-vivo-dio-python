## Introdução a POO

POO (**Programação Orientade a Objetos**) é um paradigma de programação, ou seja, uma forma de
estruturar os programas. A ideia é abstrair problemas em objetos do mundo real, onde os dois elementos chaves são: **classe** e **objeto**.  
**Classe**: Define as características e comportamentos de um objeto, mas não pode ser usada por si só.  
**Objeto**: É uma instância da classe, ou seja, um objeto dessa classe.  
 Veja um exemplo em Python:  
 **Clase**  
 Abaixo teremos a classe Cachorro. Na classe cachoro temos o CONSTRUTOR, que recebe self (que é o proprio objeto).
 Temos 2 métodos: latir e dormir.  
```python
 class Cachorro:
    
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print("Au Au Au")
    
    def dormir(self):
        self.acordado = False
        print("ZZzzZZzz...)
```

**Objeto**  
Agora podemos criar os objetos da classe cachorro, ou seja, instâncias da classe ou cachorros conhecidos.  
```python
cachorro1 = Cachorro("Mafalda", "Branco")
cachorro2 = Cachorro("Thunder", "Marrom")

cachorro1.latir()
cachorro2.dormir()
```

**Contrutores** e **Destrutores**  

**Contrutor**  
O Contrutor em Python é dado pelo método __init__, ele sempre é executado para inicializar uma instância da classe.
Serve para inicializar valores e dar o estado inicial de um objeto.  

**Destrutor**  
O destrutor em Python é dado pelo método __del__, e ele é usado quando uma instância é destruída. Em Python eles não são tão necessários quanto em C++ porque o Python tem um coletor de Lixo com lida com o gerenciamento de memória.  
```python
def __del__(self):
    ação
```
E por fim, seria chamado assim:

```Python
c = Cachorro(parametros)
del c
```
## Herança

É a capacidade de uma classe filha herdar características e comportamentos da classe pai.
Possui o benefício da reutilização do código e é de natureza transitiva onde, se a classe B herdar da classe A, todas as subclasses de B também vão herdar de A.
É importante lembrar da relação **Herança x Polimorfismo**

```Python
class A:
    pass
class B(A):
    pass
```

### Herança Simples
Herda apenas de uma classe pai

### Herança Múltipla
Herda de múltiplas classes pai. Existe o problema de ter dependência de forma cíclica, algumas linguagens não implementam esse tipo de herança.

Temos o método 
```Python
classe.__mro__
Ou
print(Classe.mro())
```
Que irá trazer a ordem de resolução das Classes.

## Encapsulamento

É um dos conceitos fundamentais em POO, descreve a ideia de agrupar dados, atributos e métodos em uma unidade, impondo restrições de acesso afim de evitar alterações acidentais.
Em Python não temos palavras reservas porém usamos convenção no nome do recruso para definir se um método/atributo é publico ou privado:  
Publico: Acessível fora da classe,  
Privado: Acessível apenas dentro da classe.  

```Python
class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade = idade
    
```

Apesar disso, o Python deixa acessar e manipular o recurso, mas por convenção não se deve mexer. Para isso, deve-se ter métodos para manipular os atributos privados. Em Java temos os métodos **getters** e **setters**

Podemos usar o **property()** que permite criar atributos gerenciados (conhecidos como propredades) quando necessitar modificar sua implementação interna sem alterar a API pública da classe. Olha como podemos usar:

```Python
class Foo:
    def __init__(self, x=None)
    self._x = x

    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        _x = self._x or 0
        _value = value or 0
        self._x = _x + _value
    
    @x.deleter
    def x(self):
        self._x = -1

foo = Foo(10) #1
foo.x = 10    #2
del foo.x     #3
```

No exemplo acima, na linha #1 criamos o objeto foo com valor de 10. Após, passamos o valor 10 para a atributo x, porém repare que o atributo da classe Foo é _x e por isso essa atribuição não é possível.
A classe Foo tem um "método" x que faria essa adição, e quando usamos o @property, mudamos sua forma de atuação e ele passa a atuar como um atributo em vez de atuar como método. O valor 10 ira para o property, que irá para o @x.setter que fará a adição e poderemos alterar o atributo _x sem alterá-la diretamente. Nesse momento é importante perceber que estamos modificando um método em atributo e por isso devemos mnipular como um atributo.

## Interfaces e Classes Abstratas

### Variáveis de classe, variáveis de instância, métodos de classe e métodos de instância

**Atributo de classe:** É compartilhado pelos objetos da classe,  
**Atributo de instância:** São diferentes para cada objeto.  
Métodos de classe: Estão ligados à classe e não ao objeto, eles têm acesso ao estado da classe, são utilizados para criar **métodos de fábrica**  
**Método estático:** Não recebe um primeiro argumento explícito, é um método vinculado à classe e não ao objeto da classe, ele não pode acessar ou modificar o estado da classe. São utilizados para criar **funções utilitárias**, ou seja, são funções que não dependem da classe necessariamente. Exemplo:  

Vamos avaliar dois cenários:
1) A classe Pessoa que contém um método para criar um objeto a partir da data de nascimento, que recebe um objeto pessoa e terá que instânciar outro objeto pessoa, o que não é ideal.

Repare que no construtor de pessoa, temos que passar nome e idade = None, caso contrário o método não iria funcionar uma vez que o construtor pede 2 argumentos.


```Python
class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    def criar_de_data_nascimento(self, ano, mes, dia, nome):
        idade = 2024 - ano
        return Pessoa(nome, idade)
    
p = Pessoa("Thiago", 31)
print(p.nome, p.idade)

p = Pessoa().criar_de_data_nascimento(1993, 9, 11, "Thiago")
print(p.nome, p.idade)


```

Dessa forma, é ideal transformar o método "criar_de_data_nascimento" em um método de classe. isso é feito usando o decorador @classmethod
Por convenção, quando usamos o @classmethod, não usamos a palavra "self" e sim "cls".

Isso significa que, como o método virou um método de classe, invocamos ele de forma diferente:

p = Classe.método_de_classe()

Por fim, criamos um método estático usando o decorador @staticmethod

```Python

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

p = Pessoa("Thiago", 31) #Thiago 31
print(p.nome, p.idade)

p = Pessoa.criar_de_data_nascimento(1993, 9, 11, "Thiago")
print(p.nome, p.idade) #Thiago 31

print(Pessoa.e_maior_idade(17)) #False
print(Pessoa.e_maior_idade(27)) #True
```
Repare que o método estático "e_maior_idade" independe de alguma instância desse objeto.

### Interfaces

Interfaces definem o que uma classe **deve** fazer e não **como** fazer. Em outras palavras a interface serve para definir um contrato, onde são declados os métodos e suas respectivas assinaturas. Em Python utilizamos **classses abstratas** para criar contratos, essas classes **não podem** ser instanciadas.  


### Classes Abstratas

Por padrão o Python não fornece classes abstratas e por isso é necessário usar o módulo abc. O abc funciona decorando métodos da classe base como abstratos e, em seguida, registrando classes concretas como implmentações da base abstrata. O método se torna abstrato quando usamos o decorador @abstractmethod

Então, de forma concisa, a classe abstrata obriga o desenvolvedor a implementar seus métodos em cada uma das classes que herdam dela.  
Para usar a classe abstrata é necessário importar o módulo ABC. Vamos criar uma classe abstrata ControleRemoto que terá os métodos ligar e desligar. Após vamos criar a classe ControleTV que herda de controle remoto:

```Python

from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto)
    pass

```

Dessa forma não será possível instanciar o ControleTV, será apresentado o erro dizendo que é obrigatório implementar os métodos.
Logo temos que fazer:

```Python

from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto)
    def ligar(self):
        print("Ligando TV...")
        print("TV ligada")
    
    def desligar(self):
        print("Desligando TV...")
        print("Tv desligada")

controle = ControleTV()
controle.ligar()
controle.desligar()

```

Podemos criar também propriedades abstratas:

```Python

from abc import ABC, abstractmethod

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

class ControleTV(ControleRemoto)
    def ligar(self):
        print("Ligando TV...")
        print("TV ligada")
    
    def desligar(self):
        print("Desligando TV...")
        print("Tv desligada")
    
    @property
    def marca(self):
        return "Marca1"

controle = ControleTV()
controle.ligar()
controle.desligar()

```

Dessa forma, teremos nossa classe funcionando.